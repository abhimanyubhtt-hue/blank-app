import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="AI Product Listing Writer", page_icon="🛍️")

st.title("🛍️ AI Product Listing Writer for Sellers")
st.write("Turn simple product descriptions into high-converting Etsy/eBay listings using open-source AI!")

product_name = st.text_input("Product Name", placeholder="e.g., Handmade Ceramic Coffee Mug")
key_features = st.text_area("Key Features / Details", placeholder="e.g., 12oz, dishwasher safe, matte finish, minimalist design")
platform = st.selectbox("Target Platform", ["Etsy", "eBay"])

if st.button("Generate Listing 🚀"):
    if not product_name or not key_features:
        st.warning("Please fill in both the product name and key features!")
    else:
        with st.spinner("Generating your listing using Open-Source AI..."):
            prompt = f"Write a compelling, SEO-optimized product listing for {platform}. Product: {product_name}. Features: {key_features}. Include a title, key features list, and product description."
            
            url = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-32B-Instruct"
            payload = json.dumps({"inputs": prompt}).encode('utf-8')
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
            
            try:
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode('utf-8'))
                generated_text = result[0]['generated_text'] if isinstance(result, list) else result.get('generated_text', str(result))
                
                st.success("Listing Generated!")
                st.markdown("### Your Generated Listing:")
                st.write(generated_text)
            except Exception as e:
                st.subheader(f"✨ Sample {platform} Listing")
                st.write(f"**Title:** Premium {product_name} - Handcrafted Quality")
                st.write(f"**Description:** Boost your sales with this beautiful {product_name}. Crafted with care, featuring: {key_features}.")

st.divider()
st.caption("Powered by Open-Source AI & Open-Weight Models | Built for Hacktoberfest")
