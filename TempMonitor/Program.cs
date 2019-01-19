using System;
using System.Threading;
using System.IO.Ports;
using System.IO;

namespace TempMonitor
{
    public class Program
    {
        const string PORT = "COM4";
        const string TEMP_COMMAND = "T";
        static SerialPort serialPort;
        const string FILE = "C:\\Users\\Vinicius\\Dropbox\\Temp.txt";
        const float alpha = 0.8f;
        static float lastTemp;
        static float currTemp;

        public static void Main(string[] args)
        {
            try {
                serialPort = new SerialPort(PORT, 9600);
                serialPort.Open();
            }
            catch(Exception e)
            {
                Console.WriteLine("Error opening port: " + e.Message);
                Console.ReadLine();
                return;
            }
            
            lastTemp = GetTemp();
            while(true)
            {
                currTemp = GetTemp();
                lastTemp = LowPassFilter();

                if (currTemp >= 0 || lastTemp >= 0)
                    WriteToFile(currTemp.ToString("0.##"), lastTemp.ToString("0.##"));

                Thread.Sleep(10000);
            }
        }

        public static float GetTemp()
        {
            float returnTemp;
            try {
                serialPort.Write(TEMP_COMMAND);
                returnTemp = float.Parse(serialPort.ReadLine());
            }
            catch(Exception)
            {
                return -1;
            }
            return returnTemp;
        }

        public static void WriteToFile(string readTemp , string filtTemp)
        {
            try {
                StreamWriter stream = new StreamWriter(FILE, true);
                stream.WriteLine(readTemp.Trim() + "\t" + filtTemp.Trim() + "\t" + DateTime.Now);
                stream.Close();
            }
            catch (Exception) { }
        }

        static float LowPassFilter()
        {
            if (currTemp < 0 || lastTemp < 0)
                return currTemp;

            return alpha * currTemp + (1 - alpha) * lastTemp;
        }
    }
}
