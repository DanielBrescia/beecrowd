Var
raio, pi, resultado: real; 
Begin
	readln(raio);
	pi:= 3.14159;
	resultado:= (4.0/3) * pi * (sqr(raio) * raio);
	writeln('VOLUME = ',resultado:0:3);  
End.
// mais avançado " resultado := (4,0/3) * pi * exp(ln(raio) * 3)