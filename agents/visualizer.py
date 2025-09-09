# agents/visualizer.py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from typing import List, Dict, Any

class VisualizerAgent:
    """
    This agent is like an artist - it turns numbers into beautiful pictures
    """
    
    def __init__(self):
        self.color_palette = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    
    def auto_visualize(self, data: pd.DataFrame, max_charts: int = 5) -> List[go.Figure]:
        """Automatically create charts based on data types - like an artist choosing the best way to paint"""
        if data.empty:
            return []
        
        charts = []
        numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
        date_cols = data.select_dtypes(include=['datetime64']).columns.tolist()
        
        chart_count = 0
        
        # 1. Bar chart for categorical data
        if categorical_cols and chart_count < max_charts:
            col = categorical_cols[0]
            value_counts = data[col].value_counts().head(10)
            fig = px.bar(
                x=value_counts.index, 
                y=value_counts.values,
                title=f'Distribution of {col}',
                color_discrete_sequence=self.color_palette
            )
            charts.append(fig)
            chart_count += 1
        
        # 2. Histogram for numeric data
        if numeric_cols and chart_count < max_charts:
            col = numeric_cols[0]
            fig = px.histogram(
                data, 
                x=col, 
                title=f'Distribution of {col}',
                color_discrete_sequence=self.color_palette
            )
            charts.append(fig)
            chart_count += 1
        
        # 3. Scatter plot if we have 2+ numeric columns
        if len(numeric_cols) >= 2 and chart_count < max_charts:
            fig = px.scatter(
                data, 
                x=numeric_cols[0], 
                y=numeric_cols[1],
                title=f'{numeric_cols[0]} vs {numeric_cols[1]}',
                color_discrete_sequence=self.color_palette
            )
            charts.append(fig)
            chart_count += 1
        
        # 4. Line chart if we have date column
        if date_cols and numeric_cols and chart_count < max_charts:
            fig = px.line(
                data, 
                x=date_cols[0], 
                y=numeric_cols[0],
                title=f'{numeric_cols[0]} over time',
                color_discrete_sequence=self.color_palette
            )
            charts.append(fig)
            chart_count += 1
        
        # 5. Correlation heatmap
        if len(numeric_cols) > 2 and chart_count < max_charts:
            corr_matrix = data[numeric_cols].corr()
            fig = px.imshow(
                corr_matrix,
                title='Correlation Heatmap',
                color_continuous_scale='RdBu'
            )
            charts.append(fig)
            chart_count += 1
        
        return charts
    
    def create_custom_chart(self, data: pd.DataFrame, chart_type: str, x_col: str, y_col: str = None) -> go.Figure:
        """Create specific chart type - like asking the artist for a specific style of painting"""
        
        if chart_type == 'bar':
            if y_col:
                fig = px.bar(data, x=x_col, y=y_col, color_discrete_sequence=self.color_palette)
            else:
                value_counts = data[x_col].value_counts()
                fig = px.bar(x=value_counts.index, y=value_counts.values, color_discrete_sequence=self.color_palette)
        
        elif chart_type == 'line':
            fig = px.line(data, x=x_col, y=y_col, color_discrete_sequence=self.color_palette)
        
        elif chart_type == 'scatter':
            fig = px.scatter(data, x=x_col, y=y_col, color_discrete_sequence=self.color_palette)
        
        elif chart_type == 'histogram':
            fig = px.histogram(data, x=x_col, color_discrete_sequence=self.color_palette)
        
        else:
            # Default to bar chart
            fig = px.bar(data, x=x_col, y=y_col, color_discrete_sequence=self.color_palette)
        
        fig.update_layout(
            title=f'{chart_type.title()} Chart: {x_col}' + (f' vs {y_col}' if y_col else ''),
            template='plotly_white'
        )
        
        return fig
    
    def create_dashboard(self, data: pd.DataFrame) -> go.Figure:
        """Create a dashboard with multiple charts - like creating a gallery of paintings"""
        numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=['Numeric Summary', 'Category Distribution', 'Correlation', 'Data Overview'],
            specs=[[{"type": "bar"}, {"type": "pie"}],
                   [{"type": "scatter"}, {"type": "table"}]]
        )
        
        # Add charts to dashboard
        if numeric_cols:
            # Numeric summary
            stats = data[numeric_cols].describe().loc['mean']
            fig.add_trace(
                go.Bar(x=stats.index, y=stats.values, name="Averages"),
                row=1, col=1
            )
        
        if categorical_cols:
            # Category distribution
            col = categorical_cols[0]
            value_counts = data[col].value_counts().head(5)
            fig.add_trace(
                go.Pie(labels=value_counts.index, values=value_counts.values, name="Distribution"),
                row=1, col=2
            )
        
        fig.update_layout(height=600, showlegend=False, title_text="Data Analysis Dashboard")
        return fig
