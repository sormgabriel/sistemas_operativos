1) usr ejecuta el programa
2) program loader va a buscar a disco 
3) program loader carga el programa en memoria
4) program loader crea un pcb del programa
5) program loader pone pcb en la cola de ready
6) scheduler asigna un pcb al cpu
7) cpu va a buscar instruccion a memoria
8) cpu evalua qu? tipo de instruccion es
9)a) si es de IO va a la cola de waiting
9)b) si no es de IO se ejecuta
9)c)
10) se incrementa pc


a)c?mo pasa de ready a run?:
	las interrupciones hacen un context switching, entonces el scheduler le el pcb al cpu hasta alguna nueva interrupci?n

b) qu? es una interrupci?n y cu?nd se dispara?:
	el mecanismo para pasar de un estado a otro es una interrupcion


c) qu? hace la cpu cuando arranca?
	el reloj le va dand se?ales para que ahga algo, si no hay nada que hacwr queda idle
d) quien crea el pcb?
	con new  del programa  crea el pcb y setea todo

modos usuario procesa una instruccion funciona bajo clock
modo kernel procesa interrupcion el clock es ignorado

a medida que madura un programa aumenta su prioridad; tenemos que implentar un roundrobin+prioridad

  



