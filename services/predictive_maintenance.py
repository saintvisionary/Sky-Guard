import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from models.maintenance import Maintenance
from models import db
import numpy as np

def predict_maintenance(aircraft_id):
    # Fetch maintenance records for the given aircraft
    maintenance_records = Maintenance.query.filter_by(aircraft_id=aircraft_id).all()
    if not maintenance_records:
        return None

    # Prepare data for predictive model
    data = [(record.date, record.details) for record in maintenance_records]
    df = pd.DataFrame(data, columns=['date', 'details'])
    
    # Feature extraction: calculate days since last maintenance and encode details
    df['days_since_last'] = (df['date'] - df['date'].shift()).fillna(pd.Timedelta(days=0)).dt.days
    df['details_encoded'] = df['details'].apply(lambda x: len(x))  # Dummy encoding for details

    # Define features (X) and target (y) variables
    X = df[['days_since_last', 'details_encoded']].values[1:]  # Exclude the first record
    y = (df['date'].values[1:] - df['date'].values[0]).astype('timedelta64[D]').astype(int)

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train the model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_scaled, y)

    # Predict the next maintenance date
    next_maintenance_days = model.predict(scaler.transform([[df['days_since_last'].iloc[-1], df['details_encoded'].iloc[-1]]]))
    next_maintenance_date = df['date'].iloc[-1] + np.timedelta64(int(next_maintenance_days[0]), 'D')
    
    return next_maintenance_date
