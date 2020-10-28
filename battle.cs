using System;
using System.Linq;
using System.Security.Cryptography;
using System.Threading;

namespace Battle
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please insert your username below!");
            string name = Console.ReadLine();
            Do("sleep", "1");
            Do("clear");
            Console.WriteLine("Beat the boss!");
            Do("sleep", "25");

            Random rnd = new Random();
            int boss_health = 125;
            int user_health = 100;
            int battle = 0;

            while ((boss_health >= 1) && (user_health >= 1))
            {
                Do("clear");
                int boss_damage = rnd.Next(6, 12);
                int user_damage = rnd.Next(1, 16);
                int mortal = rnd.Next(8, 20);
                int user_heal = rnd.Next(4, 16);
                int boss_heal = rnd.Next(2, 12);
                battle += 1;

                Console.WriteLine($"ROUND {battle}!");
                Do("sleep", "12");
                Console.WriteLine("Boss health: " + Convert.ToString(boss_health));
                Console.WriteLine($"{name.Trim()} health: " + Convert.ToString(user_health));
                Do("sleep", "1");

                if (user_health==100)
                {
                    Do("nl", "1");
                    Console.WriteLine("You can use only hit/heal.");
                }
                string skema = Console.ReadLine();

                Do("nl", "1");
                if (skema.ToLower()=="hit")
                {
                    int r = rnd.Next(1, 6);
                    if (r==1)
                    {
                        int boss_mortal = user_damage + mortal;
                        boss_health -= boss_mortal;
                        Console.WriteLine($"MORTAL HIT! {name.Trim()} punched for {boss_mortal}DMG!");
                    }
                    else
                    {
                        boss_health -= user_damage;
                        Console.WriteLine($"{name.Trim()} punched for {user_damage}DMG!");
                    }
                }
                else if (skema.ToLower()=="heal")
                {
                    user_health += user_heal;
                    Console.WriteLine($"{name.Trim()} increased health with {user_heal}HP");
                }
                else
                {
                    Console.WriteLine("!WRONG VALUE!");
                    boss_health -= user_damage;
                    Console.WriteLine($"{name.Trim()} punched for {user_damage}DMG!");
                }

                Do("sleep", "25");
                int choice = rnd.Next(1, 6);
        
                if (boss_health >= 1)
                    if (!(choice <= 4) && (boss_health<=55))
                    {
                        boss_health += boss_heal;
                        Console.WriteLine($"Boss increased health with {boss_heal}HP");
                    }
                    else
                    {
                        user_health -= boss_damage;
                        Console.WriteLine($"Boss punched you for {boss_damage}");
                    }
                else
                {
                    break;
                }

                Do("nl", "1");
                Console.WriteLine("Next round in 4.5s");
                Do("sleep", "45");
            }
            Do("clear");
            Do("nl", "1");
            if (user_health < boss_health)
            {
                Console.WriteLine("You got owned by BOSS!");
            }
            else if (user_health > boss_health)
            {
                Console.WriteLine("You defeated BOSS, Good job!");
            }
            else
            {
                Console.WriteLine("How tf you both died???");
            }
            Console.WriteLine("Boss HP: " + boss_health.ToString());
            Console.WriteLine($"{name.Trim()} HP: " + user_health.ToString());

        }
        static void Do(string task, string ms="None")
        {
            if (task.ToLower()=="clear")
            {
                Console.Clear();
            }
            else if (task.ToLower()=="sleep")
            {
                if (ms.ToLower()=="none")
                {
                    ms = "1000";
                }
                int x = ms.Length;
                if (x<4)
                {
                    x = 4 - Convert.ToInt32(x);
                    foreach (int val in Enumerable.Range(0, x))
                    {
                        ms = ms + "0";
                    }
                }
                int mil = Convert.ToInt32(ms);
                Thread.Sleep(Convert.ToInt32(mil));
            }
            else if (task.ToLower()=="nl")
            {
                if ((Convert.ToInt32(ms)==0) || (ms.ToLower()=="none"))
                {
                    ms = "1";
                }
                int lines = Convert.ToInt32(ms);
                foreach (int x in Enumerable.Range(0, lines))
                {
                    Console.Write(Environment.NewLine);
                }
            }
            else { Error(); }
            
            static void Error()
            {
                Console.WriteLine("Something went Wrong..");
                Do("sleep", "25");
                Console.WriteLine("Closing..");
                Do("sleep", "15");
                Environment.Exit(0);
            }
        }
    }
}
