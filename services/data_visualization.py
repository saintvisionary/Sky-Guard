import matplotlib.pyplot as plt
import io
import base64

def generate_maintenance_chart(data):
    # Generate a maintenance chart
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['maintenance_cost'], marker='o')
    plt.title('Maintenance Costs Over Time')
    plt.xlabel('Date')
    plt.ylabel('Maintenance Cost')
    plt.grid(True)

    # Save the chart to a string buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_bytes = buf.getvalue()
    buf.close()

    # Encode the image to base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    return img_base64
