import streamlit as st

# Updated cat data with local images
cats = [
    {
        "id": 1,
        "name": "Persian Cat (Grey)",
        "price": "₹15,500",
        "desc": "A beautiful grey Persian cat, known for its soft coat and calm demeanor.",
        "img": "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"
    },
    {
        "id": 2,
        "name": "Persian Cat (White)",
        "price": "₹16,000",
        "desc": "A pure white Persian cat, elegant and extremely friendly.",
        "img": "/mnt/data/persian cat white.webp"
    },
    {
        "id": 3,
        "name": "Persian Cat (Black)",
        "price": "₹15,000",
        "desc": "A rare and stunning black Persian cat, calm and loyal.",
        "img": "https://cdn2.thecatapi.com/images/bpc.jpg"
    },
    {
        "id": 4,
        "name": "Siamese Cat",
        "price": "₹12,000",
        "desc": "Sleek, elegant, vocal and affectionate.",
        "img": "https://cdn2.thecatapi.com/images/ai6Jps4sx.jpg"
    },
    {
        "id": 5,
        "name": "Persian Cat (Brown Fluffy Kitten)",
        "price": "₹14,500",
        "desc": "Fluffy brown Persian kitten with big round eyes, playful and cuddly.",
        "img": "/mnt/data/cat.jpg"
    },
    {
        "id": 6,
        "name": "Maine Coon",
        "price": "₹18,000",
        "desc": "Big, fluffy, and very gentle breed.",
        "img": "https://cdn2.thecatapi.com/images/OD3N9Zzdo.jpg"
    }
]

# Streamlit config
st.set_page_config(page_title="Pet Aura - Cat Pet Shop", layout="wide")
st.title("🐱 Pet Aura - Cat Pet Shop")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_cat" not in st.session_state:
    st.session_state.selected_cat = None
if "order_placed" not in st.session_state:
    st.session_state.order_placed = False

def go_to_page(page):
    st.session_state.page = page

def select_cat(cat):
    st.session_state.selected_cat = cat
    go_to_page("details")

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.button("🏠 Home", on_click=lambda: go_to_page("home"))
st.sidebar.button("🐾 View All Cats", on_click=lambda: go_to_page("catalog"))

# Home Page
if st.session_state.page == "home":
    st.subheader("Welcome to Pet Aura 🐾")
    st.markdown("Your one-stop shop for adorable cat companions! Explore and adopt your furry friend today.")
    st.image("https://cdn2.thecatapi.com/images/8b8.jpg", width=600)

# Catalog Page
elif st.session_state.page == "catalog":
    st.subheader("🐱 Our Cat Collection")
    cols = st.columns(3)
    for idx, cat in enumerate(cats):
        with cols[idx % 3]:
            st.image(cat["img"], width=200)
            st.markdown(f"**{cat['name']}**")
            st.markdown(cat["price"])
            if st.button(f"View Details - {cat['id']}"):
                select_cat(cat)

# Cat Details Page
elif st.session_state.page == "details":
    cat = st.session_state.selected_cat
    if cat:
        st.image(cat["img"], width=400)
        st.subheader(cat["name"])
        st.markdown(f"**Price:** {cat['price']}")
        st.markdown(cat["desc"])
        if st.button("🐾 Adopt Now"):
            go_to_page("order")
    else:
        st.warning("No cat selected. Go back to the catalog.")
        go_to_page("catalog")

# Order Form Page
elif st.session_state.page == "order":
    st.subheader("🐾 Place Your Order")
    with st.form("order_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        address = st.text_area("Delivery Address")
        pricing_method = st.selectbox("Pricing Method", ["Full Payment", "Installments"])
        cat_name = st.session_state.selected_cat["name"] if st.session_state.selected_cat else "Unknown"
        submitted = st.form_submit_button("Confirm Order")
        if submitted:
            st.session_state.order_placed = True
            st.session_state.customer = {
                "name": name,
                "email": email,
                "phone": phone,
                "address": address,
                "pricing_method": pricing_method,
                "cat": cat_name
            }
            go_to_page("confirmation")

# Order Confirmation Page
elif st.session_state.page == "confirmation":
    if st.session_state.order_placed:
        customer = st.session_state.customer
        st.success("🎉 Order Placed Successfully!")
        st.markdown(f"**Thank you, {customer['name']}!**")
        st.markdown(f"🐱 Adopted Cat: **{customer['cat']}**")
        st.markdown(f"📧 Email: {customer['email']}")
