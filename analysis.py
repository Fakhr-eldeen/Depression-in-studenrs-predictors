import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def generate_dashboard(data):
    plots = []

    # 1. Bar Plot: Distribution of Gender
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Gender', data=data, palette='pastel')
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plots.append(save_plot_to_html())

    # 2. Pie Chart: Breakdown of Dietary Habits
    plt.figure(figsize=(6, 6))
    data['Dietary Habits'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue', 'orange', 'green'])
    plt.title('Dietary Habits Breakdown')
    plt.ylabel('')
    plots.append(save_plot_to_html())

    # 3. Scatter Plot: CGPA vs Depression
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='CGPA', y='Depression', data=data, alpha=0.6)
    plt.title('CGPA vs Depression')
    plt.xlabel('CGPA')
    plt.ylabel('Depression')
    plots.append(save_plot_to_html())

    # 4. Histogram: Distribution of Academic Pressure
    plt.figure(figsize=(6, 4))
    sns.histplot(data['Academic Pressure'], kde=True, color='purple')
    plt.title('Distribution of Academic Pressure')
    plt.xlabel('Academic Pressure')
    plt.ylabel('Frequency')
    plots.append(save_plot_to_html())

    # 5. Box Plot: Sleep Duration vs Depression
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='Sleep Duration', y='Depression', data=data, palette='muted')
    plt.title('Sleep Duration vs Depression')
    plt.xlabel('Sleep Duration')
    plt.ylabel('Depression')
    plots.append(save_plot_to_html())

    # 6. Line Plot: CGPA Trend by Age
    plt.figure(figsize=(8, 4))
    data_sorted = data.sort_values('Age')  # Sort by Age for a meaningful trend
    plt.plot(data_sorted['Age'], data_sorted['CGPA'], marker='o', linestyle='-', color='blue')
    plt.title('CGPA Trend by Age')
    plt.xlabel('Age')
    plt.ylabel('CGPA')
    plots.append(save_plot_to_html())

    # Combine all plots as HTML
    return ''.join(plots)

def save_plot_to_html():
    """Save the current plot to an HTML-compatible string."""
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()
    return f'<img src="data:image/png;base64,{plot_data}" style="margin:20px;" alt="Plot">'
