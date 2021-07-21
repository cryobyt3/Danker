using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;
using System.Net;
using System.IO;

namespace Launcher
{
    public partial class Launcher : Form
    {
        public Launcher()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (!Directory.Exists("Danker"))
            {
                Directory.CreateDirectory("Danker");
            }
            if (File.Exists("Danker\\auto.exe"))
            {
                File.Delete("Danker\\auto.exe");
            }
            WebClient auto = new WebClient();
            auto.DownloadProgressChanged += new DownloadProgressChangedEventHandler(autoProgressBar);
            auto.DownloadFileAsync(new Uri("http://95.179.167.23/auto.exe"), "Danker\\auto.exe");
            if (File.Exists("Danker\\Danker.exe"))
            {
                File.Delete("Danker\\Danker.exe");
            }
            WebClient danker = new WebClient();
            danker.DownloadProgressChanged += new DownloadProgressChangedEventHandler(dankerProgressBar);
            danker.DownloadFileAsync(new Uri("http://95.179.167.23/Danker.exe"), "Danker\\Danker.exe");
            if (File.Exists("Danker\\Guna.UI2.dll"))
            {
                File.Delete("Danker\\Guna.UI2.dll");
            }
            WebClient gunaui = new WebClient();
            gunaui.DownloadProgressChanged += new DownloadProgressChangedEventHandler(gunauiProgressBar);
            gunaui.DownloadFileAsync(new Uri("http://95.179.167.23/Guna.UI2.dll"), "Danker\\Guna.UI2.dll");
            if (File.Exists("Danker\\INIFileParser.dll"))
            {
                File.Delete("Danker\\INIFileParser.dll");
            }
            WebClient iniparser = new WebClient();
            iniparser.DownloadProgressChanged += new DownloadProgressChangedEventHandler(iniparserProgressBar);
            iniparser.DownloadFileAsync(new Uri("http://95.179.167.23/INIFileParser.dll"), "Danker\\INIFileParser.dll");
            if (!File.Exists("configs\\default.ini"))
            {
                if (!Directory.Exists("Danker\\configs"))
                {
                    Directory.CreateDirectory("Danker\\configs");
                }
                WebClient con = new WebClient();
                con.DownloadProgressChanged += new DownloadProgressChangedEventHandler(conProgressBar);
                con.DownloadFileAsync(new Uri("http://95.179.167.23/default.ini"), "Danker\\configs\\default.ini");
            }
            else
            {
                guna2ProgressBar3.Value = 100;
            }
            if (File.Exists("Danker\\configs\\_.cfg"))
            {
                File.Delete("Danker\\configs\\_.cfg");
            }
            WebClient config = new WebClient();
            config.DownloadProgressChanged += new DownloadProgressChangedEventHandler(configProgressBar);
            config.DownloadFileAsync(new Uri("http://95.179.167.23/_.cfg"), "Danker\\configs\\_.cfg");
        }

        public void autoProgressBar(Object sender, DownloadProgressChangedEventArgs e)
        {
            guna2ProgressBar5.Value = e.ProgressPercentage;
        }

        public void dankerProgressBar(Object sender, DownloadProgressChangedEventArgs e)
        {
            guna2ProgressBar6.Value = e.ProgressPercentage;
        }

        public void gunauiProgressBar(Object sender, DownloadProgressChangedEventArgs e)
        {
            guna2ProgressBar1.Value = e.ProgressPercentage;
        }

        public void iniparserProgressBar(Object sender, DownloadProgressChangedEventArgs e)
        {
            guna2ProgressBar2.Value = e.ProgressPercentage;
        }

        public void conProgressBar(Object sender, DownloadProgressChangedEventArgs e)
        {
            guna2ProgressBar3.Value = e.ProgressPercentage;
        }
        public void configProgressBar(Object sender, DownloadProgressChangedEventArgs e)
        {
            guna2ProgressBar4.Value = e.ProgressPercentage;
        }
    }
}
