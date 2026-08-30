var
  n, area, raio :real;
Begin
	n := 3.14159;
	readln(raio);
	area := sqr(raio) * n;
	write('A=',area:0:4);
End.