<h1 align="center"> Cyber-AC </h1>
<em> Proyecto Final Diseño de Compiladores </em>

<em> A01283076 Antonio Díaz Ramos </em>
<em> A01275834 Citlalli Rosario Alonzo Mateos</em>

## Avance 1: 
Sintáxis completa del programa, incluye declaración de clases (con sus atributos y métodos, y herencia simple), variables, funciones y el main. 
Hemos realizado diversas pruebas y consideramos que toda la sintáxis funciona y está completa, al igual que contempla lo necesario para que el compilador funcione
al momento de revisar la sintáxis del lenguaje de programación.

La sintáxis que actualmente el programa maneja es la declaración del nombre de programa, clases, atributos, métodos, funciones, variables y estatutos como if, if-else, from, while-do, read y write. 

```
program proyectocompilador;

class Animal 
{
   attribute:
   public int x;
   private float s;

   method:
   private void prueba (int ys) 
   {
      x = 5;
      y[3] = x;
      

      if(x+2 equal 2)
      {
         p = x;
      }

      else 
      {
         metodo(x);
      }
      
   }

   public int hello (int y, int z)
   {
      y=3;

      while (x+2*3) do 
      {
         mato(2);
         y = 2;
      }
      return e;
   }
};

class Dog : public Animal 
{
   attribute:
   public int x;
   private float s;

   method:
   private void prueba (int y) 
   {
      if(5>3)
      {
         x=w;
      }

      return x*2;
   }


   public int hello (int y, int z)
   {
      x=3;
      
      return e;
   }
};

var 
   Dog perro;
   int edad;
   int edad2;
   float peso;
   char caracter;
   int array[1];
   float array2[2][3];


func int suma (int y);
var 
   int edad3;
{
   
   x = 5.3;
   y = x;
   z = suma(x) + a - 6;

   read (x);
   read (x[2], x);
   read (x,w,x);
   write ('t', "jajaja");

   x='w';
   return x+2;
   
}


func void suma (int x, float y);
{
   x=2;
   y = p.ladra(temp1);

   y = p.ladra;

   p.come(x);
   p.duerma(3, y);
   p.juega(4.8);
   p.corre('a');
   p.atri1;

   write("buenas", p.edad, p.sum(7, 3.4));

   if (x > p.edad and y < p.anos ) {
      y[1] = p.edad;
      if (v < p.calculo) {
         u = 1 + p;
      }
   }

   while (p.animal) do {
      x = p.corre(3);
   }

   from s = p.t > 2 to p.ala equal 5 do {
      m1(x, 8);
   }
}

func void suma (char z);
{
   y=3;
}

main()
{
   x=2;
   write(x+2);

   p.come(x);
   p.duerma(3, y);
   p.juega(4.8);
   p.corre('a');
   p.atri1;

   from x = 2+3 to y do
   {
      read(w);
   }

   y = p.ladra(temp);

   y = p.ladra;

   write("buenas", p.edad, p.sum(7, 3.4));

   if (x > p.edad and y < p.anos ) {
      y[1] = p.edad;
      if (v < p.calculo) {
         u = 1 + p;
      }
   }

   while (p.animal) do {
      x = p.corre(3);
   }

   from s = p.t > 2 to p.ala equal 5 do {
      m1(x, 8);
   }
   
}
```

## Avance 2
Se agrego el diccionario del cubo semántico, la tabla de variables y el directorio de funciones. El cubo semántico ya tiene los operadores derechos, operadores izquierdos, y operandos con su respectivo resultado, además, se hizo la función que devuelve el resultado. La tabla de variables ya guarda las variables de todo el programa junto con su scope y tipo. El directorio de funciones aun no está conectado a la tabla de variables pero ya guarda el nombre de la función. 

## Avance 3
Se empiezan a generar los cuadruplos de las expresiones de asignación, lectura y escritura. También se generan los cuadruplos de while. 

## Avance 4
Se realizó la asignación de direcciones virtuales a las variables y constantes. Ya se genera el código intermedio de if y for, addemás, los cuadruplos se crean tomando en cuenta las direcciones virtuales.

```
program Compilador;

var
    int i;
    int a;
    int b;
    float c;
    float d;
    int e;
    int f;
    float g;
    char x;
    bool hola;
    int j;

func int suma (int y);
var 
   int varF1;
   
{
   read(varF1);
   
}

main() {

    for j = 1 to i + a * b do {
        b = i + a;
    }

    write ("Terminafor"); 

    if (a > b) {
        read(a, b);
    } else {
        a = e + f;
        write(e, "Hola", a);
    }

    if (c < d) {
        g = c + d;
    }
    
    while (c < d) do 
    {
        g = d;
    }

    c = d + e + i * a;

}

```

<img width="238" alt="Screen Shot 2022-11-04 at 19 08 21" src="https://user-images.githubusercontent.com/62078976/200094343-a9bba9d5-f2f4-498c-9ff2-d39859168882.png">



