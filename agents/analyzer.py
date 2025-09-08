# agents/analyzer.py
import pandas as pd
from openai import OpenAI
import json
from typing import Dict, List, Any

class AnalyzerAgent:
    """
    This agent is like a detective - it looks at data and finds interesting patterns
    """
    
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def basic_statistics(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Calculate basic statistics - like counting and measuring things"""
        if data.empty:
            return {"error": "No data to analyze"}
        
        numeric_data = data.select_dtypes(include=['number'])
        categorical_data = data.select_dtypes(include=['object'])
        
        stats = {
            "numeric_summary": numeric_data.describe().to_dict() if not numeric_data.empty else {},
            "categorical_summary": {col: data[col].value_counts().head().to_dict() 
                                  for col in categorical_data.columns} if not categorical_data.empty else {},
            "correlations": numeric_data.corr().to_dict() if len(numeric_data.columns) > 1 else {}
        }
        return stats
    
    def ai_insights(self, data_info: Dict, user_question: str) -> str:
        """Use AI to generate insights - like having a smart friend explain the data"""
        
        # Prepare data summary for AI
        data_summary = f"""
        Data Summary:
        - Rows: {data_info.get('rows', 0)}
        - Columns: {data_info.get('columns', 0)}
        - Column Names: {data_info.get('column_names', [])}
        - Data Types: {data_info.get('data_types', {})}
        - Missing Values: {data_info.get('missing_values', {})}
        - Sample Data: {json.dumps(data_info.get('sample_data', {}), indent=2)}
        
        User Question: {user_question}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a data analyst. Analyze the provided data and answer the user's question with clear, actionable insights."},
                    {"role": "user", "content": data_summary}
                ],
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating AI insights: {e}"
    
    def find_trends(self, data: pd.DataFrame) -> List[str]:
        """Find trends in the data - like spotting patterns"""
        trends = []
        
        # Look for time-based trends
        date_columns = data.select_dtypes(include=['datetime64']).columns
        numeric_columns = data.select_dtypes(include=['number']).columns
        
        if len(date_columns) > 0 and len(numeric_columns) > 0:
            trends.append("Time series data detected - can analyze trends over time")
        
        # Look for correlations
        if len(numeric_columns) > 1:
            corr_matrix = data[numeric_columns].corr()
            high_corr = []
            for i in range(len(corr_matrix.columns)):
                for j in range(i+1, len(corr_matrix.columns)):
                    if abs(corr_matrix.iloc[i, j]) > 0.7:
                        high_corr.append(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]}")
            
            if high_corr:
                trends.append(f"Strong correlations found between: {', '.join(high_corr)}")
        
        # Look for missing data patterns
        missing_data = data.isnull().sum()
        high_missing = missing_data[missing_data > len(data) * 0.1]
        if not high_missing.empty:
            trends.append(f"Columns with significant missing data: {list(high_missing.index)}")
        
        return trends if trends else ["No obvious trends detected in current analysis"]
