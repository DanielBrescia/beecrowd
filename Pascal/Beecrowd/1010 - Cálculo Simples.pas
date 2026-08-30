var
a, b, c, d, e, f, Apagar: real; 
begin
	readln(a, b, c);
	readln(d, e, f);
	Apagar := (b * c) + (e * f);
	writeln('VALOR A PAGAR: R$ ',Apagar:0:2);  
end.