import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO



# PAGE CONFIG


st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered"
)



# CSS


st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    color: #777;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)



# TITLE


st.markdown(
    '<div class="main-title">🔳 QR Code Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Create QR from URL or Image</div>',
    unsafe_allow_html=True
)



# MODE


mode = st.radio(
    "Choose QR Type",
    [
        "🔗 URL to QR",
        "🖼️ Image to QR"
    ],
    horizontal=True
)



# INPUT


data = None
uploaded_image = None


if mode == "🔗 URL to QR":

    url = st.text_input(
        "🔗 Enter URL",
        placeholder="https://example.com"
    )

    if url.strip():
        data = url.strip()


else:

    uploaded_image = st.file_uploader(
        "🖼️ Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image:

        image = Image.open(
            uploaded_image
        )

        st.image(
            image,
            caption="Selected Image",
            width=300
        )

        # For this basic version,
        # QR stores the image filename.
        data = uploaded_image.name



# COLOR SETTINGS


st.subheader("🎨 QR Customization")

col1, col2 = st.columns(2)

with col1:

    qr_color = st.color_picker(
        "QR Color",
        "#000000"
    )

with col2:

    background_color = st.color_picker(
        "Background Color",
        "#FFFFFF"
    )



# GENERATE


if st.button(
    "🚀 Generate QR Code",
    type="primary",
    use_container_width=True
):

    if not data:

        st.error(
            "❌ Please provide a URL or upload an image."
        )

    else:

        try:

           
            # CREATE QR
           
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=12,
                border=4
            )

            qr.add_data(data)

            qr.make(
                fit=True
            )

            qr_image = qr.make_image(
                fill_color=qr_color,
                back_color=background_color
            ).convert("RGB")


        
            # SHOW QR
          

            st.subheader(
                "✨ Your QR Code"
            )

            st.image(
                qr_image,
                width=400
            )


           
            # DOWNLOAD
            

            buffer = BytesIO()

            qr_image.save(
                buffer,
                format="PNG"
            )

            buffer.seek(0)

            st.download_button(
                label="⬇️ Download QR",
                data=buffer.getvalue(),
                file_name="qr_code.png",
                mime="image/png",
                use_container_width=True
            )

            st.success(
                "✅ QR Code generated successfully!"
            )


        except Exception as error:

            st.error(
                f"❌ Error: {error}"
            )