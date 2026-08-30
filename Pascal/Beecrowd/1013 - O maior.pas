Var
  a, b, c, maiorab, maior: real;
Begin
	readln(a);
	readln(b);
	readln(c);
	maiorab:= ((a + b + abs(a - b)) / 2);
	maior:= ((maiorab + c + abs(maiorab - c)) / 2);
	writeln(maior:0:0,' eh o maior');   
End.