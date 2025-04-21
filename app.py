import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="Secure Encryption App", layout="centered")

st.title("🔐 Secure Data Encryption App")
st.write("Encrypt and decrypt text using a secure key.")

# --- Key Handling ---
st.subheader("Key Management")

key_option = st.radio("Select Key Option", ["Generate New Key", "Use Existing Key"])

key = None  # Define key globally

if key_option == "Generate New Key":
    key = Fernet.generate_key()
    st.success("Key Generated Successfully!")
    st.code(key.decode())

    # Add a download button
    st.download_button("Download Key", key, file_name="secret.key")

else:
    key_input = st.text_input("Paste your existing Fernet key:")
    if key_input:
        try:
            # Try decoding to ensure valid key
            Fernet(key_input.encode())
            key = key_input.encode()
            st.success("Key accepted.")
        except:
            st.error("Invalid key. Make sure it's a valid Fernet key.")

# --- Functions ---
def encrypt_message(msg, key):
    f = Fernet(key)
    return f.encrypt(msg.encode()).decode()

def decrypt_message(msg, key):
    f = Fernet(key)
    return f.decrypt(msg.encode()).decode()

# --- Encryption/Decryption Section ---
st.subheader("Encryption / Decryption")

mode = st.radio("Mode", ["Encrypt", "Decrypt"])
text = st.text_area("Enter your text:")

if st.button("Submit"):
    if not text:
        st.warning("Please enter text.")
    elif not key:
        st.warning("Please generate or enter a valid key.")
    else:
        try:
            if mode == "Encrypt":
                result = encrypt_message(text, key)
                st.success("Encrypted Text:")
                st.code(result)
            else:
                result = decrypt_message(text, key)
                st.success("Decrypted Text:")
                st.code(result)
        except Exception as e:
            st.error(f"Operation failed: {str(e)}")