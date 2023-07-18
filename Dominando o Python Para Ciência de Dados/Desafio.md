<head>
<h3> Desafio Criando Um Sistema Bancário com Python </h3>
<p>Desafio elaborado por Guilherme Arthur de Carvalho</p>
</head>
<body>
<h4>Narrativa</h4>
<p>Fomos contratados por um grande banco para desenvolver o seu novo sistema.</p>
<p>Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.</p>
<p>Para a primeira versão do sistema, devemos implementar apenas três operações, quais sejam depósito, saque e extrato</p>

<h4>Objetivo Geral</h4>
<p>Criar um sistema bancário com as operações:
	<ol>
		<li>Sacar</li>
		<li>Depositar</li>
		<li>Visualizar Extrato</li>
	</ol>
</p>

<h4>Objetivos Específicos</h4>

<h6>Operação de Depósito</h6>
<p>Deve ser possível depositar valores positivos para a minha conta bancária</p>
<p>A v1 do projeto trabalha apenas com um usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e a conta bancária.</p>
<p>Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato</p>

<h6>Operação de Saque</h6>
<p>O sistema deve permitir realizar três saques diários com limite máximo de 500 reais por saque.</p>
<p>Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não é possível sacar o dinheiro porque falta saldo.</p>
<p>Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato</p>

<h6>Operação de Extrato</h6>
<p>Essa operação deve listar todos os depósitos e saques realizados na conta</p>
<p>No fim da listagem deve ser exibido o saldo atual da conta</p>
<p> Se o extrato estiver em branco, exibir a mensagem "Não foram realizadas movimentações"</p>
<p> Oe valores devem ser exibidos utilizando o formato R$ XXX.XX, ex: R$ 1500.45</p>
</body>