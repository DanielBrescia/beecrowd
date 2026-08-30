var 
id, HorasTrabalhadas : integer;
PorHora, Salario : real;
Begin
	readln(id);
	readln(HorasTrabalhadas);
	readln(PorHora);
	Salario := HorasTrabalhadas * PorHora;
	writeln('NUMBER = ',id);
	writeln('SALARY = U$ ',Salario:0:2);	  
End.