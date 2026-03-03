import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Custom Software Solutions | Team MGIS-350", layout="wide")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        background-color: #004b87;
        color: white;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_index=True)

# --- HEADER SECTION ---
st.title("🚀 Custom Software Solutions")
st.subheader("Empowering Small Businesses with Robust Data Intelligence")
st.write("---")

# --- MISSION STATEMENT ---
col1, col2 = st.columns([2, 1])
with col1:
    st.header("Our Mission")
    st.info("""
    To provide local Rochester businesses with seamless, data-driven tools that 
    simplify operations and fuel expansion. We believe that technology should be 
    accessible, reliable, and tailored to the unique pulse of your storefront.
    """)
with col2:
    st.header("Core Values")
    st.write("✅ **Reliability:** Data integrity is our priority.")
    st.write("✅ **Simplicity:** Python-powered tools anyone can run.")
    st.write("✅ **Precision:** Accurate reporting for smarter growth.")

# --- THE PROJECT: SCOOPS AND SMILES ---
st.write("---")
st.header("The Scoops & Smiles Enterprise Suite")
st.markdown("#### *A Custom-Built Solution for the Rochester Ice Cream Expansion*")

tab1, tab2, tab3 = st.tabs(["Inventory Management", "Financial Reporting", "Technical Specs"])

with tab1:
    st.subheader("Smart Stock Tracking")
    st.write("""
    - **Flavor-Specific Inventory:** Track Vanilla, Chocolate, Cookies & Cream, and more by the ounce.
    - **Multi-Location Support:** Separate data silos for every new shop in the Rochester region.
    - **Restock Logic:** Automated expense calculation when purchasing 5-gallon containers.
    """)

with tab2:
    st.subheader("Financial Intelligence")
    st.write("""
    - **Monthly Income Statements:** View profitability by location or for the entire franchise.
    - **Sales Trending:** Identify which flavors are moving (and which aren't) to optimize orders.
    - **Fixed/Variable Cost Tracking:** Automated accounting for rent, labor ($15k/mo), and utilities.
    """)

with tab3:
    st.subheader("System Requirements")
    st.code("""
    Language: Python 3.x
    Database: Local Persistent Storage (SQLite/CSV)
    Hardware: Standard Laptop Compatible
    Libraries: Standard Library + Setup Documentation provided
    """)

# --- PRICING & DATA PREVIEW (From Appendix) ---
st.write("---")
with st.expander("View Menu & Variable Cost Logic"):
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Flavor Costs (5 Gallon)**")
        st.table({
            "Flavor": ["Vanilla", "Chocolate", "Cookies & Cream", "Cookie Dough"],
            "Cost": ["$1.80", "$1.80", "$1.90", "$1.95"]
        })
    with c2:
        st.write("**Sales Pricing**")
        st.table({
            "Size": ["Kiddie", "Small", "Medium", "Large"],
            "Price": ["$3.00", "$3.50", "$4.00", "$4.50"]
        })

# --- FOOTER / CONTACT ---
st.write("---")
st.write("Prepared for: **Saunders College of Business | MGIS-350**")
if st.button("Contact Our Team for a Needs Assessment"):
    st.balloons()
    st.success("Meeting Request Sent! We will bring our list of project questions.")
