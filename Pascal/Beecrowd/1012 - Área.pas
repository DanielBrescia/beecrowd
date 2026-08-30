Var
	a, b, c, pi, atriangulo, acirculo, atrapezio, aquadrado, aretangulo : real;
Begin
	readln(a);
  readln(b);
  readln(c);
  pi:= 3.14159;
	atriangulo:= (a * c) / 2;
	acirculo:= pi * sqr(c);
	atrapezio:= ((a + b) * c) / 2;
	aquadrado:= sqr(b);
	aretangulo:= a * b;
	writeln('TRIANGULO: ',atriangulo:0:3);
	writeln('CIRCULO: ',acirculo:0:3);
	writeln('TRAPEZIO: ',atrapezio:0:3);
	writeln('QUADRADO: ',aquadrado:0:3);
	writeln('RETANGULO: ',aretangulo:0:3);
End.