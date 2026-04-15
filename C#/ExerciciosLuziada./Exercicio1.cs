using System.Diagnostics.CodeAnalysis;

namespace Exercicios
{
    public class Exercicio1
    {
        public void tabuada(int numero = 1)
        {
            for (int i = 1; i < 11; i++)
            {
                var valor = numero * i;
                Console.WriteLine($"{numero} * {i} = {valor}");
            }
        }

        public double media(params double[] numeros)
        {
            double total = 0;
            foreach (double numero in numeros)
            {
                total += numero;
            }
            return total/numeros.Length;
        }

        //Calcular
        public void somarPar()
        {
            int soma = 0;
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Insira o numero: ");
                var numero = int.Parse(Console.ReadLine()!);
                
                if(numero%2 == 0)
                {
                    soma += numero;
                }
            }
            Console.WriteLine($"A soma é igual {soma}");
        }

        public void definirAprovado(){
            double media_nota = 0;
            double[] notas = new double[3];

            for (int i = 0; i < 3; i++){
                Console.WriteLine($"Insira a {i+1}ª nota: ");
                notas[i]= double.Parse(Console.ReadLine()!);
            }
            media_nota = media(numeros: notas);
            var aprovado = media_nota >= 10;
            var reprovado = media_nota < 8;

            if (aprovado){
                Console.WriteLine($"A sua média é {media_nota} - Aprovado");
            }else if (reprovado){
                Console.WriteLine($"A sua média é {media_nota} - Reprovado");
            }else{
                Console.WriteLine($"A sua média é {media_nota} - Recurso");
            }
            
        }

        public void maioresQue10(){
            int m_10 = 0;

            for (int i = 1; i < 6; i++){
                Console.WriteLine($"Insira o {i}º número: ");
                var numero = int.Parse(Console.ReadLine()!);
                if(numero > 10)
                    m_10++;
            }
            Console.WriteLine($"Números maiores que 10 são {m_10}");
        }

        public void indiceMasaCorporal(double massa, double altura){
            Console.WriteLine($"Indice de massa corporal é igual a {massa/(altura*altura)}");
        }

        public void celciusToFahrenheit(double temperauraCelcius)
        {
            var fahrenheit = temperauraCelcius * 1.8 + 32;
            Console.WriteLine($"A temperatura em Fahrenheit é {fahrenheit}");
        }

        public void velocidade(double distancia, double tempo){
            var velocidade = distancia / tempo;
            Console.WriteLine($"A velocidade é igual a {velocidade}");
        }
        
    }
}