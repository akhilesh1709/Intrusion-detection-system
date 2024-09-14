import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from preprocessing.preprocess import preprocess_data
from utils.helpers import rename_columns, change_order_rows
import os

# Custom CSS for larger margins and spacing
# Custom CSS for even larger margins and spacing

def main():
    st.title("Intrusion Detection System")

    st.header("Instructions")
    st.write("""
        **Follow these steps:**
        1. Click the button below to download the required software.
        2. Install the downloaded software `zeroshield.exe` on your system.
        3. Run the software to generate a CSV file.
        4. Upload the generated CSV file in the next section to scan for intrusions.
    """)

    # Add download button for the software
    software_path = "zeroshield.exe"  # Update this path
    if os.path.exists(software_path):
        with open(software_path, "rb") as file:
            st.download_button(
                label="Download Software",
                data=file,
                file_name="intrusion_detection_software.exe",
                mime="application/octet-stream"
            )
    else:
        st.error("Software file not found. Please check the file path.")


    st.header("Upload and Scan for Attacks")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            # Try reading the CSV file
            df = pd.read_csv(uploaded_file)
            df = rename_columns(df)
            df = change_order_rows(df)
            print(df.columns)

            if df.empty:
                st.error("The uploaded file is empty. Please upload a valid CSV file.")
                return

            # Display data preview
            st.write("Data Preview:")
            st.write(df.head())

            # If button clicked, start attack detection
            if st.button("Check for Attacks"):
                # Preprocess the data
                processed_data = preprocess_data(df)

                # Load the model
                try:
                    model = joblib.load('model/model.joblib')
                except Exception as e:
                    st.error(f"Error loading model: {e}")
                    return

                # Make predictions
                try:
                    predictions = model.predict(processed_data)

                    # Display results
                    total_records = len(predictions)
                    total_attacks = sum(predictions)
                    total_normal = total_records - total_attacks
                    attack_percentage = total_attacks / total_records * 100
                    normal_percentage = 100 - attack_percentage

                    st.write("Results:")
                    st.write(f"Total records: {total_records}")
                    st.write(f"Records classified as attacks: {total_attacks}")
                    st.write(f"Percentage of attacks: {attack_percentage:.2f}%")

                    # Plot pie chart for the results
                    labels = ['Normal Traffic', 'Attacks']
                    sizes = [total_normal, total_attacks]
                    colors = ['#1f77b4', '#ff7f0e']
                    explode = (0.1, 0)  # explode the attack slice for emphasis

                    fig, ax = plt.subplots()
                    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                            shadow=True, startangle=90)
                    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

                    # Display pie chart
                    st.pyplot(fig)

                    # Display a sample of detected attacks
                    if total_attacks > 0:
                        st.write("Sample of detected attacks:")
                        attacks = df.loc[predictions == 1].head()
                        st.write(attacks)
                    else:
                        st.write("No attacks detected.")

                except Exception as e:
                    st.error(f"Error making predictions: {e}")

        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty or has no columns to parse. Please upload a valid CSV file.")
        except Exception as e:
            st.error(f"Error processing the file: {e}")

if __name__ == "__main__":
    main()
