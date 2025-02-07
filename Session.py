import numpy as np
import pandas as pa
import streamlit as st

class AppDeployment:
    @staticmethod
    def streamlit():
        # User input for name
        user_name = st.text_input("Enter your name:", "Samyak")  # Default name set to 'Samyak'

        if user_name:
            st.title(f"Welcome, {user_name}! 🎉")  
            st.write(f"Hello, {user_name}! This is a simple example of Streamlit.")

        # Sample DataFrame
        data = pa.DataFrame({"c1": [10, 20, 30, 40], "c2": ["A", "B", "C", "D"]})
        st.write("Table Data:", data)

        # Generate random chart data
        chart_data = pa.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.write("Random Data:", chart_data)

        # Display Charts
        st.write("Line Chart")
        st.line_chart(chart_data)

        st.write("Bar Chart")
        st.bar_chart(chart_data)

        st.write("Area Chart")
        st.area_chart(chart_data)

        # Celebration Balloons
        st.balloons()

        # Camera Input & Download Option
        photo = st.camera_input(f"Smile, {user_name}! 😊")  
        if photo:
            st.download_button(
                label="Download Image",
                data=photo.getvalue(),
                file_name=f"{user_name}_captured_photo.png",  # Personalized file name
                mime="image/png",
            )

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    AppDeployment.streamlit()
