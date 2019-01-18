using System;
using System.Threading;
using System.IO.Ports;
using System.IO;

namespace TempMonitor
{
    class Program
    {
        const string PORT = "COM4";
        const string TEMP_COMMAND = "T";
        static SerialPort serialPort;
        static string readString;
        const string FILE = "C:\\Users\\Vinicius\\Dropbox\\Temp.txt";

        static void Main(string[] args)
        {
            serialPort = new SerialPort(PORT, 9600);
            serialPort.Open();

            while(true)
            {
                readString = GetTemp();

                if (!string.IsNullOrEmpty(readString))
                    WriteToFile(readString);

                Thread.Sleep(10000);
            }
        }

        static string GetTemp()
        {
            serialPort.Write(TEMP_COMMAND);
            return serialPort.ReadLine();
        }

        static void WriteToFile(string temp)
        {
            try {
                StreamWriter stream = new StreamWriter(FILE, true);
                stream.WriteLine(temp.Trim() + "\t" + DateTime.Now);
                stream.Close();
            }
            catch (Exception) { }
        }
    }
}
