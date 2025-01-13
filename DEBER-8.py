using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // Crear una lista con las asignaturas del curso
        List<string> asignaturas = new List<string> { "Matemáticas", "Física", "Química", "Historia", "Lengua" };

        // Crear una lista para almacenar las notas
        List<double> notas = new List<double>();

        // Preguntar al usuario la nota de cada asignatura
        foreach (string asignatura in asignaturas)
        {
            Console.Write($"¿Qué nota has sacado en {asignatura}? ");
            if (double.TryParse(Console.ReadLine(), out double nota))
            {
                notas.Add(nota);
            }
            else
            {
                Console.WriteLine("Entrada no válida. Por favor, introduce un número.");
                return;
            }
        }

        // Mostrar las asignaturas con sus respectivas notas
        for (int i = 0; i < asignaturas.Count; i++)
        {
            Console.WriteLine($"En {asignaturas[i]} has sacado {notas[i]}");
        }

        // Mostrar las asignaturas del curso
        Console.WriteLine("Las asignaturas del curso son:");
        foreach (string asignatura in asignaturas)
        {
            Console.WriteLine($"- {asignatura}");
        }

        // Crear una lista con los números del 1 al 10
        List<int> numeros = Enumerable.Range(1, 10).ToList();

        // Mostrar los números en orden inverso, separados por comas
        numeros.Reverse();
        Console.WriteLine(string.Join(", ", numeros));

        // Crear una lista para almacenar los números ganadores
        List<int> numerosGanadores = new List<int>();

        // Preguntar al usuario por 6 números ganadores
        for (int i = 0; i < 6; i++)
        {
            Console.Write($"Introduce el número ganador {i + 1}: ");
            if (int.TryParse(Console.ReadLine(), out int numero))
            {
                numerosGanadores.Add(numero);
            }
            else
            {
                Console.WriteLine("Entrada no válida. Por favor, introduce un número entero.");
                return;
            }
        }

        // Ordenar la lista de menor a mayor
        numerosGanadores.Sort();

        // Mostrar los números ganadores ordenados
        Console.WriteLine("Los números ganadores ordenados son:");
        Console.WriteLine(string.Join(", ", numerosGanadores));
    }
}
