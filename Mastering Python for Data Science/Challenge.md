<head>
<h3> Challenge Creating a Banking System with Python </h3>
<p>Challenge prepared by Guilherme Arthur de Carvalho</p>
</head>
<body>
<h4>Narrative</h4>
<p>We were hired by a big bank to develop their new system.</p>
<p>This bank wants to modernize its operations and has chosen the Python language for that.</p>
<p>For the first version of the system, we should implement only three operations, namely deposit, withdrawal and statement</p>

<h4>General Objective</h4>
<p>Create a banking system with the operations:
<ol>
<li>Withdraw</li>
<li>Deposit</li>
<li>View Statement</li>
</ol>
</p>
<h4>Specific Objectives</h4>

<h6>Deposit Operation</h6>
<p>It should be possible to deposit positive amounts to my bank account</p>
<p>The v1 of the project only works with one user, so we don't have to worry about identifying the branch number and bank account number.</p>
<p>All deposits must be stored in a variable and displayed in the statement operation</p>
<h6>Withdraw Operation</h6>
<p>The system should allow three daily withdrawals with a maximum limit of 500 BRL per withdrawal.</p>
<p>If the user has no account balance, the system should display a message stating that it is not possible to withdraw the money because there is no balance.</p>
<p>All withdrawals must be stored in a variable and displayed in the statement operation</p>

<h6>Statement Operation</h6>
<p>This operation should list all deposits and withdrawals made to the account</p>
<p>The current account balance should be displayed at the end of the listing</p>
<p> If the statement is blank, display the message "No transactions were carried out"</p>
<p> The values must be displayed using the BRL XXX.XX format, eg BRL 1500.45</p>