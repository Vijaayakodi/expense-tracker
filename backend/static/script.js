// =============================
// Expense Tracker Frontend
// =============================

// Backend API URL
const API_URL = "http://127.0.0.1:5000";

// Wait until page loads
document.addEventListener("DOMContentLoaded", () => {

    // Load existing data
    loadTransactions();
    loadSummary();

    // Form Submit
    document
        .getElementById("transactionForm")
        .addEventListener("submit", addTransaction);

});


// =============================
// ADD TRANSACTION
// =============================

async function addTransaction(event){

    event.preventDefault();

    const transaction = {

        title: document.getElementById("title").value,

        amount: parseFloat(document.getElementById("amount").value),

        category: document.getElementById("category").value,

        type: document.getElementById("type").value,

        transaction_date: document.getElementById("transaction_date").value,

        notes: document.getElementById("notes").value

    };

    try{

        const response = await fetch(`${API_URL}/transactions`,{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(transaction)

        });

        const result = await response.json();

        if(result.success){

            alert("✅ Transaction Added Successfully");

            document.getElementById("transactionForm").reset();

            loadTransactions();

            loadSummary();

        }else{

            alert(result.message);

        }

    }catch(error){

        console.error(error);

        alert("Server Error");

    }

}



// =============================
// LOAD TRANSACTIONS
// =============================

async function loadTransactions(){

    try{

        const response = await fetch(`${API_URL}/transactions`);

        const result = await response.json();

        const table = document.getElementById("transactionTable");

        table.innerHTML="";

        result.data.forEach(transaction=>{

            table.innerHTML += `

            <tr>

                <td>${transaction.title}</td>

                <td>₹${transaction.amount}</td>

                <td>${transaction.category}</td>

                <td>${transaction.type}</td>

                <td>${transaction.transaction_date}</td>

                <td>

                    <button onclick="deleteTransaction(${transaction.id})">

                        Delete

                    </button>

                </td>

            </tr>

            `;

        });

    }catch(error){

        console.error(error);

    }

}



// =============================
// LOAD SUMMARY
// =============================

async function loadSummary(){

    try{

        const response = await fetch(`${API_URL}/summary`);

        const result = await response.json();

        document.getElementById("balance").innerText =
        "₹"+result.data.balance;

        document.getElementById("income").innerText =
        "₹"+result.data.total_income;

        document.getElementById("expense").innerText =
        "₹"+result.data.total_expense;

    }catch(error){

        console.error(error);

    }

}



// =============================
// DELETE TRANSACTION
// =============================

async function deleteTransaction(id){

    const confirmDelete = confirm("Delete this transaction?");

    if(!confirmDelete) return;

    try{

        const response = await fetch(`${API_URL}/transactions/${id}`,{

            method:"DELETE"

        });

        const result = await response.json();

        if(result.success){

            loadTransactions();

            loadSummary();

        }

    }catch(error){

        console.error(error);

    }

}