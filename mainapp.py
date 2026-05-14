import streamlit as st
import pandas as pd
from datetime import datetime
from home import FinanceTracker
import plotly.graph_objects as go
import datetime as dt


def main():
    st.set_page_config(
        page_title="Personal Finance Tracker",
        page_icon="💰",
        layout="wide"
    )

    st.markdown("""
    <style>

    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #050816, #0d1b2a, #132238);
        color: white;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #06111f, #0d223d);
        border-right: 2px solid cyan;
    }

    /* Page title */
    .page-title {
        background: linear-gradient(135deg, #00c6ff, #0072ff, #00e5ff);
        color: white;
        padding: 20px;
        border-radius: 18px;
        font-size: 2rem;
        font-weight: 800;
        text-align: center;
        border: 3px solid cyan;
        box-shadow: 0px 0px 25px rgba(0,255,255,0.4);
        margin-bottom: 25px;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(90deg, #00e5ff, #00bcd4);
        color: black !important;
        font-weight: 700;
        border-radius: 12px;
        border: none;
        padding: 10px 18px;
        transition: 0.3s ease-in-out;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 15px cyan;
    }

    /* Form submit buttons */
    div[data-testid="stFormSubmitButton"] button {
        background: linear-gradient(90deg, #00e5ff, #00bcd4);
        color: black !important;
        font-weight: 700;
        border-radius: 12px;
        border: none;
    }

    /* Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 18px;
        border-radius: 18px;
        border: 1px solid cyan;
        box-shadow: 0 0 12px rgba(0,255,255,0.15);
        margin-bottom: 15px;
        transition: 0.3s;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 20px rgba(0,255,255,0.35);
    }

    /* Metrics */
    div[data-testid="metric-container"] {
        background: rgba(255,255,255,0.06);
        border: 1px solid cyan;
        padding: 12px;
        border-radius: 15px;
    }

    </style>
    """, unsafe_allow_html=True)

    if "tracker" not in st.session_state:
        st.session_state.tracker = FinanceTracker()

    tracker = st.session_state.tracker

    # Sidebar
    with st.sidebar:
        st.title("💰 Finance Tracker")

        page = st.radio(
            "Navigation",
            [
                "🏠 Home",
                "➕ Add Income",
                "➖ Add Expense",
                "📜 History",
                "📊 Summary"
            ]
        )

        st.divider()
        st.subheader("📌 Quick Stats")
        st.metric("Income", f"₹{tracker.calculate_total_income():.2f}")
        st.metric("Expense", f"₹{tracker.calculate_total_expense():.2f}")
        st.metric("Balance", f"₹{tracker.get_remaining_balance():.2f}")

    # HOME PAGE
    if page == "🏠 Home":
        st.markdown(
            '<div class="page-title">💰 Personal Finance Tracker</div>',
            unsafe_allow_html=True
        )
        st.write("Hello there, Isn't  it hard to track where our hard earned money is going?? , Worry not..here i am to help you track your income and expenses, I am Your Personal friendly Finance Tracker..")
        st.write("This dashboard is designed to help you manage your finances effectively. You can easily add your income and expenses, view your transaction history, and analyze your spending patterns with interactive charts. Let's get started on your journey to better financial health!")
        st.write("Use the sidebar to navigate through different sections of the app. You can add new transactions, view your history, and check out the summary for insights into your financial habits.")
        st.write("I will help you with each and evry step, so don't hesitate to explore and make the most out of this tool. Happy tracking! 😊")
        st.markdown("""
        ### Welcome 👋 
        Track your money smarter with this beautiful finance dashboard.

        ### What you can do here:
        - ✅ Add your income records
        - ✅ Add daily expenses
        - ✅ View transaction history
        - ✅ Monitor remaining balance
        - ✅ Analyze spending visually
        - ✅ Track category-wise expenses
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="feature-card">
                <h4>📈 Income Tracking</h4>
                <p>Store salary, freelance, investments and more.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-card">
                <h4>📉 Expense Monitoring</h4>
                <p>Track food, shopping, bills, rent, and other expenses.</p>
            </div>
            """, unsafe_allow_html=True)

        st.info("💡 Tip: Check Summary page for charts and insights.")

    # ADD INCOME
    elif page == "➕ Add Income":
        st.markdown(
            '<div class="page-title">➕ Add Income</div>',
            unsafe_allow_html=True
        )

        with st.form("income_form"):
            source = st.selectbox(
                "Income Source",
                ["Salary", "Freelance", "Investment", "Other"]
            )
            amount = st.number_input("Amount", min_value=0.01)
            date = st.date_input("Date", value=dt.date.today())
            description = st.text_input("Description")

            submitted = st.form_submit_button("Add Income")

            if submitted:
                success, message = tracker.add_income(
                    source, amount, date, description
                )
                if success:
                    st.success(message)
                else:
                    st.error(message)

    # ADD EXPENSE
    elif page == "➖ Add Expense":
        st.markdown(
            '<div class="page-title">➖ Add Expense</div>',
            unsafe_allow_html=True
        )

        with st.form("expense_form"):
            category = st.selectbox(
                "Category",
                [
                    "Education",
                    "Entertainment",
                    "Food & Dining",
                    "Healthcare",
                    "Monthly subscriptions",
                    "Shopping",
                    "Transportation",
                    "Utilities",
                    "Rent",
                    "Other"
                ]
            )

            amount = st.number_input("Amount", min_value=0.01)
            date = st.date_input("Date", value=dt.date.today())
            description = st.text_input("Description")

            submitted = st.form_submit_button("Add Expense")

            if submitted:
                success, message = tracker.add_expense(
                    category, amount, date, description
                )
                if success:
                    st.success(message)
                else:
                    st.error(message)

    # HISTORY
    elif page == "📜 History":
        st.markdown(
            '<div class="page-title">📜 Transaction History</div>',
            unsafe_allow_html=True
        )

        data = tracker.get_all_transactions()

        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, width="stretch", hide_index=True)
        else:
            st.info("No transactions available.")

        st.write(f"### Remaining Balance: ₹{tracker.get_remaining_balance():.2f}")

    # SUMMARY
    elif page == "📊 Summary":
        st.markdown(
            '<div class="page-title">📊 Financial Summary</div>',
            unsafe_allow_html=True
        )

        total_income = tracker.calculate_total_income()
        total_expense = tracker.calculate_total_expense()
        balance = tracker.get_remaining_balance()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Income", f"₹{total_income:.2f}")

        with col2:
            st.metric("Expense", f"₹{total_expense:.2f}")

        with col3:
            st.metric("Balance", f"₹{balance:.2f}")

        category_data = tracker.get_category_wise_spending()

        st.subheader("Income vs Expense")

        fig_bar = go.Figure()
        fig_bar.add_trace(
            go.Bar(
                x=["Income", "Expense"],
                y=[total_income, total_expense]
            )
        )

        fig_bar.update_layout(
            title="Income vs Expense Comparison",
            xaxis_title="Type",
            yaxis_title="Amount (₹)"
        )

        st.plotly_chart(fig_bar, width="stretch")

        if category_data:
            st.subheader("Category-wise Expense Distribution")

            categories = list(category_data.keys())
            amounts = list(category_data.values())

            fig_donut = go.Figure(
                data=[
                    go.Pie(
                        labels=categories,
                        values=amounts,
                        hole=0.5
                    )
                ]
            )

            fig_donut.update_layout(
                title="Expense Distribution by Category"
            )

            st.plotly_chart(fig_donut, width="stretch")


if __name__ == "__main__":
    main()