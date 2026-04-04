using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EstructuraDeDatos
{
    public class EjemploArrays
    {
        public static void Ejecutar()
        {
            int[] arreglo = new int[10];
            Random random = new Random();

            // Generar valores aleatorios
            for (int i = 0; i < arreglo.Length; i++)
            {
                arreglo[i] = random.Next(1, 51);
            }

            Console.WriteLine("Arreglo principal:");

            // Recorrido con for
            for (int i = 0; i < arreglo.Length; i++)
            {
                Console.Write("[" + i + "]=" + arreglo[i] + " ");
            }

            Console.WriteLine("\n\nRecorrido con foreach:");

            foreach (int num in arreglo)
            {
                Console.Write(num + " ");
            }

            // Modificación del arreglo
            Console.WriteLine("\n\nModificando arreglo...");

            for (int i = 0; i < arreglo.Length; i++)
            {
                if (arreglo[i] % 2 != 0)
                {
                    arreglo[i] = -1;
                }

                arreglo[i] = arreglo[i] * i;
            }

            // Mostrar arreglo modificado
            Console.WriteLine("Arreglo modificado:");
            for (int i = 0; i < arreglo.Length; i++)
            {
                Console.Write(arreglo[i] + " ");
            }

            // Búsqueda lineal
            int valorBuscado = 10;
            bool encontrado = false;

            for (int i = 0; i < arreglo.Length; i++)
            {
                if (arreglo[i] == valorBuscado)
                {
                    Console.WriteLine("\nValor encontrado en la posición: " + i);
                    encontrado = true;
                    break;
                }
            }

            if (!encontrado)
            {
                Console.WriteLine("\nEl valor " + valorBuscado + " no se encontró en el arreglo.");
            }
        }
    }
}
