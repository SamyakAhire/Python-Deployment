import numpy as np
import pandas as pa
import streamlit as st


class App_Deployment:
    def streamlit():
        st.title("welcome Everyone")  # streamlit run./file_name.py
        st.write("This is a simple example of streamlit")

        st.write("This is a simple example of streamlit")  # printing the text
        data = pa.DataFrame({"c1": [10, 20, 30, 40], "c2": ["A", "B", "C", "D"]})
        st.write(data)  # printing the data in the form of table

        # for i in range(0,100):
        #     st.progress(i)                    #progress bar
        # st.checkbox("Check",value=True)       #checkbox

        chart_data = pa.DataFrame(
            np.random.randn(20, 3), columns=["a", "b", "c"]
        )  # random data and converting it into table by using DataFrame
        st.write("Random Data")
        st.write(chart_data)

        st.balloons()  # celebration of the completion of the task

        st.write("Line Chart")
        st.line_chart(chart_data)  # line chart

        st.write("Bar Chart")
        st.bar_chart(chart_data)  # Bar chart

        st.write("Area Chart")
        st.area_chart(chart_data)  # Area chart

        # st.color_picker("Pick Color")    #color picker

        photo = st.camera_input("Smile")  # camera input

        if photo:
            # Convert the image to bytes for downloading
            st.download_button(
                label="Download",
                data=photo.getvalue(),  # Get the image bytes
                file_name="captured_photo.png",  # Filename for download
                mime="image/png",  # MIME type
            )


App_Deployment.streamlit()
