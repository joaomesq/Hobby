using System;

namespace Entrega
{
    class Program
    {
        public static void Main(String[] args)
        {
            Entrega[] entregas = new Entrega[2];

            entregas[0] = new Entrega("Lossambo");
            entregas[1] = new Entrega("Cidade Alta");

            Console.WriteLine(entregas[0]);
        }
    }
}