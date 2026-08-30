var 
nome : string;
SalarioFixo, Vendas, Comicao, SalarioFinal : real;
Begin
	readln(nome);
	readln(SalarioFixo);
	readln(Vendas);
	comicao := vendas * 0.15;
	SalarioFinal := SalarioFixo + comicao;
	writeln('TOTAL = R$ ',SalarioFinal:0:2);  
End.