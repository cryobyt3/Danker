using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using IniParser;
using IniParser.Model;


namespace Danker
{
    public partial class Main : Form
    {
        public FileIniDataParser parser = new FileIniDataParser();
        public string token_path = "";
        public string private_path = "";

        public Main()
        {
            InitializeComponent();
            con_value.Text = "";
            con_value.Text = "None";
            if (File.Exists(Directory.GetCurrentDirectory() + "\\token"))
            {
                guna2HtmlLabel2.ForeColor = Color.Green;
                guna2HtmlLabel2.Text = "Found!";
                token_path = "token";
                guna2HtmlLabel1.Text = "Status: waiting for private key...";
            }
            else
            {
                guna2HtmlLabel1.Text = "Status: waiting for start...";
            }
        }

        private void guna2CircleButton1_Click(object sender, EventArgs e)
        {
            Environment.Exit(0);
        }

        private void guna2Button1_Click(object sender, EventArgs e)
        {
            if (guna2HtmlLabel2.ForeColor == Color.Green && guna2HtmlLabel4.ForeColor == Color.Green)
            {
                if (guna2RadioButton1.Checked)
                {
                    Process p = new Process();
                    p.StartInfo.FileName = Directory.GetCurrentDirectory() + "\\auto.exe";
                    p.StartInfo.Arguments = "2";
                    p.Start();
                    guna2HtmlLabel1.Text = "Status: started...";
                    guna2HtmlLabel1.Text = "Status: waiting for action...";
                }
                else if (guna2RadioButton3.Checked)
                {
                    Process p = new Process();
                    p.StartInfo.FileName = Directory.GetCurrentDirectory() + "\\auto.exe";
                    p.StartInfo.Arguments = "3";
                    p.Start();
                    guna2HtmlLabel1.Text = "Status: selling...";
                    guna2HtmlLabel1.Text = "Status: waiting for action...";
                }
                else if (guna2RadioButton2.Checked)
                {
                    Process p = new Process();
                    p.StartInfo.FileName = Directory.GetCurrentDirectory() + "\\auto.exe";
                    p.StartInfo.Arguments = "1";
                    p.Start();
                    guna2HtmlLabel1.Text = "Status: started...";
                    guna2HtmlLabel1.Text = "Status: waiting for action...";
                }
                else
                {
                    MessageBox.Show("Select an option!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else if (guna2HtmlLabel2.ForeColor == Color.Green)
            {
                MessageBox.Show("Private key is required!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else if (guna2HtmlLabel4.ForeColor == Color.Green)
            {
                MessageBox.Show("No token file selected!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                Process p = new Process();
                p.StartInfo.FileName = Directory.GetCurrentDirectory() + "\\auto.exe";
                p.StartInfo.Arguments = "0";
                p.Start();
                guna2HtmlLabel1.Text = "Status: started...";
                p.WaitForExit();
                if (File.Exists(Directory.GetCurrentDirectory() + "\\token"))
                {
                    guna2HtmlLabel2.ForeColor = Color.Green;
                    guna2HtmlLabel2.Text = "Found!";
                    token_path = "token";
                    guna2HtmlLabel1.Text = "Status: waiting for private key...";
                }
                else
                {
                    guna2HtmlLabel1.Text = "Status: waiting for action...";
                }
            }
        }

        private void guna2ComboBox1_DropDown(object sender, EventArgs e)
        {
            Array s = Directory.GetFiles(Directory.GetCurrentDirectory() + "\\configs", "*.ini");
            guna2ComboBox1.Items.Clear();
            foreach (string file in s)
            {
                guna2ComboBox1.Items.Add(file);
            }
        }

        private void guna2ComboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (guna2ComboBox1.SelectedIndex != -1)
            {
                con_value.Text = Path.GetFileName(guna2ComboBox1.SelectedItem.ToString());

                IniData data = parser.ReadFile(guna2ComboBox1.SelectedItem.ToString());

                guna2DataGridView1.Rows.Clear();
                guna2DataGridView1.Rows.Add("beg", data["ENABLED"]["beg"]);
                guna2DataGridView1.Rows.Add("search", data["ENABLED"]["search"]);
                guna2DataGridView1.Rows.Add("fish", data["ENABLED"]["fish"]);
                guna2DataGridView1.Rows.Add("hunt", data["ENABLED"]["hunt"]);
                guna2DataGridView1.Rows.Add("dig", data["ENABLED"]["dig"]);
                guna2DataGridView1.Rows.Add("pm", data["ENABLED"]["pm"]);
                guna2DataGridView1.Rows.Add("check-items", data["OPTIONS"]["check-items"]);
                guna2DataGridView1.Rows.Add("loop", data["OPTIONS"]["loop"]);
                guna2DataGridView1.Rows.Add("channel", data["OPTIONS"]["channel"]);
                guna2DataGridView1.Rows.Add("wait-between-commands-range-1", data["TIMINGS"]["wait-between-commands-range-1"]);
                guna2DataGridView1.Rows.Add("wait-between-commands-range-2", data["TIMINGS"]["wait-between-commands-range-2"]);
                guna2DataGridView1.Rows.Add("cycles-range1", data["TIMINGS"]["cycles-range1"]);
                guna2DataGridView1.Rows.Add("cycles-range2", data["TIMINGS"]["cycles-range2"]);
                guna2DataGridView1.Rows.Add("cycle-time", data["TIMINGS"]["cycle-time"]);
                guna2DataGridView1.Rows.Add("cycle-time-range1", data["TIMINGS"]["cycle-time-range1"]);
                guna2DataGridView1.Rows.Add("cycle-time-range2", data["TIMINGS"]["cycle-time-range2"]);
            }
            else
            {
                guna2ComboBox1.SelectedIndex = guna2ComboBox1.FindString(con_value.Text);
            }
        }

        private void guna2DataGridView1_CellValueChanged(object sender, DataGridViewCellEventArgs e)
        {
            if (con_value.Text != null)
            {
                IniData data = parser.ReadFile("configs\\" + con_value.Text);

                var row = guna2DataGridView1.Rows[e.RowIndex].Cells[e.ColumnIndex - 1].Value.ToString();
                var val = guna2DataGridView1.Rows[e.RowIndex].Cells[e.ColumnIndex].Value.ToString();
                data["OPTIONS"][row] = val;
                parser.WriteFile("configs\\" + con_value.Text, data, Encoding.ASCII);
            }
        }

        private void guna2ComboBox1_DropDownClosed(object sender, EventArgs e)
        {
            if (guna2ComboBox1.SelectedIndex == -1){
                guna2ComboBox1.SelectedIndex = guna2ComboBox1.FindString(con_value.Text);
            }
        }

        private void guna2Button3_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog file = new OpenFileDialog())
            {
                file.InitialDirectory = Directory.GetCurrentDirectory();
                file.Filter = "Private key (*.ppk)|*.ppk";
                file.FilterIndex = 2;
                file.RestoreDirectory = true;

                if (file.ShowDialog() == DialogResult.OK)
                {
                    private_path = file.FileName;
                    guna2HtmlLabel4.ForeColor = Color.Green;
                    guna2HtmlLabel4.Text = "Found!";
                    if (guna2HtmlLabel2.ForeColor != Color.Red)
                    {
                        guna2HtmlLabel1.Text = "Status: waiting for action...";
                    }
                    else
                    {
                        Environment.Exit(0);
                    }
                }
            }
        }

        private void guna2Button2_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog file = new OpenFileDialog())
            {
                file.InitialDirectory = Directory.GetCurrentDirectory();
                file.Filter = "Token file|token";
                file.FilterIndex = 2;
                file.RestoreDirectory = true;

                if (file.ShowDialog() == DialogResult.OK)
                {
                    token_path = file.FileName;
                    guna2HtmlLabel2.ForeColor = Color.Green;
                    guna2HtmlLabel2.Text = "Found!";
                    if (guna2HtmlLabel4.ForeColor != Color.Red)
                    {
                        guna2HtmlLabel1.Text = "Status: waiting for action...";
                    }
                    else
                    {
                        guna2HtmlLabel1.Text = "Status: waiting for private key...";
                    }
                }
            }
        }

        private void guna2ImageButton1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("To be implemented!", "Not Exactly X", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void guna2ImageButton3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("To be implemented!", "Not Exactly X", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void guna2ImageButton2_Click(object sender, EventArgs e)
        {
            MessageBox.Show("To be implemented!", "Not Exactly X", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
