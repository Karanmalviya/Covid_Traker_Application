import requests
import bs4
import tkinter as tk
from tkinter import ttk
import main
from tkinter import messagebox



#global varibles
n3 = ""
root = ""


def get_html_data(url):
    data = requests.get(url)
    return data


def get_country_data():
    global root,n


    country_name = n3.get()
    if country_name == '':
            messagebox.showwarning("Alert","Please Select the Country")
    else:
            url = "https://www.worldometers.info/coronavirus/country/"+country_name
            html_data = get_html_data(url)
            bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
            info_div = bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
            all_data=""

            for i in range(3):
                text = info_div[i].find("h1",class_=None).get_text()
                count = info_div[i].find("span", class_=None).get_text()
                all_data = all_data + text + " " + count + "\n"

            country_title.config(text=country_name)
            country_label.config(text=all_data)

def back_to_main():
    root.destroy()
    main.run()
    


def run():
    global n3,root,country_title,country_label
    root = tk.Tk()
    root.title('Counry Data')
    
    width = 700
    height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable('False','False')
    root.config(bg="#ffffff")
    img = tk.PhotoImage(file="icon/covid.png")
    root.iconphoto(root,img)

    label_t = tk.Label(root,text="",bg="#ffffff").grid(row=0,column=5)
    img_btn = tk.PhotoImage(file="icon/back.png")
    img_size = img_btn.subsample(20,20)
    back_button = tk.Button(root, image=img_size, command= back_to_main)
    back_button.grid(row = 0 , column = 0)
    back_button.config(bg="#ffffff")
    back_button.config(borderwidth=0)

    country_title = tk.Label(root, text="         ",font=("Papyrus", 15,"bold"),background = '#FFFFFF')
    country_title.grid(column=5,row=13, padx=10)
            
    country_label = tk.Label(root, text="         ",font=("Papyrus", 12),background = '#FFFFFF')
    country_label.grid(column=5,row=14, padx=10)
      
    label_t = tk.Label(root, text = "Country Wise Cases",background = "#ffffff", foreground ="#000000",font = ("Papyrus", 25))
    label_t.grid(row = 0, column = 5)
    label_t.config(fg='#297d5d')
    ttk.Label(root, text = "Select the Country :",background = "#ffffff",font = ("Papyrus", 14)).grid(column = 4,row = 8, padx = 10, pady = 25)


    # Combobox creation
    n3 = tk.StringVar()
    #get_country_data
    countrychoosen = ttk.Combobox(root, width = 27, textvariable = n3,state="readonly")
      
    # Adding combobox drop down list
    countrychoosen['values'] = (
                            'US',
                            'India',
                            'Brazil',
                            'UK',
                            'Russia',
                            'Turkey',
                            'France',
                            'Iran',
                            'Argentina',
                            'Colombia',
                            'Spain',
                            'Italy',
                            'Indonesia',
                            'Germany',
                            'Mexico',
                            'Poland',
                            'South-Africa',
                            'Philippines',
                            'Ukraine',
                            'Malaysia',
                            'Peru',
                            'Netherlands',
                            'Iraq',
                            'Japan',
                            'Czechia',
                            'Chile',
                            'Canada',
                            'Thailand',
                            'Bangladesh',
                            'Israel',
                            'Pakistan',
                            'Belgium',
                            'Romania',
                            'Sweden',
                            'Portugal',
                            'Morocco',
                            'Serbia',
                            'Kazakhstan',
                            'Cuba',
                            'Switzerland',
                            'Hungary',
                            'Jordan',
                            'Nepal',
                            'Vietnam',
                            'Austria',
                            'UAE',
                            'Tunisia',
                            'Greece',
                            'Lebanon',
                            'Georgia',
                            'Guatemala',
                            'Saudi-Arabia',
                            'Belarus',
                            'Costa-Rica',
                            'Sri-Lanka',
                            'Ecuador',
                            'Bolivia',
                            'Bulgaria',
                            'Azerbaijan',
                            'Panama',
                            'Paraguay',
                            'Myanmar',
                            'Kuwait',
                            'Slovakia',
                            'Croatia',
                            'Palestine',
                            'Uruguay',
                            'Ireland',
                            'Venezuela',
                            'Honduras',
                            'Dominican-Republic',
                            'Denmark',
                            'Ethiopia',
                            'Libya',
                            'Lithuania',
                            'S.-Korea',
                            'Oman',
                            'Egypt',
                            'Mongolia',
                            'Slovenia',
                            'Moldova',
                            'Bahrain',
                            'Armenia',
                            'Kenya',
                            'Qatar',
                            'Bosnia-and-Herzegovina',
                            'Zambia',
                            'Nigeria',
                            'Algeria',
                            'North-Macedonia',
                            'Norway',
                            'Kyrgyzstan',
                            'Botswana',
                            'Uzbekistan',
                            'Albania',
                            'Latvia',
                            'Afghanistan',
                            'Estonia',
                            'Mozambique',
                            'Finland',
                            'Montenegro',
                            'Zimbabwe',	
                            'Namibia',	
                            'Ghana',
                            'Uganda	',
                            'Cyprus	',
                            'Cambodia',	
                            'El-Salvador',	
                            'Australia',	
                            'Rwanda',
                            'China',
                            'Singapore',
                            'Cameroon',	
                            'Maldives',	
                            'Jamaica',	
                            'Luxembourg',	
                            'Senegal',	
                            'Malawi',
                            'Ivory Coast',	
                            'DRC',	
                            'Angola',
                            'Réunion',	
                            'Guadeloupe',	
                            'Fiji',
                            'Trinidad-and-Tobago',
                            'Eswatini',	
                            'Madagascar ',
                            'Martinique',	
                            'Suriname',	
                            'French-Polynesia',	
                            'French-Guiana',
                            'Sudan',
                            'Cabo-Verde',	
                            'Malta',
                            'Mauritania',	
                            'Syria',
                            'Guyana',
                            'Guinea',
                            'Gabon',
                            'Togo',
                            'Benin',
                            'Laos',
                            'Haiti',
                            'Seychelles',
                            'Bahamas',
                            'Mayotte',
                            'Somalia',
                            'Belize',
                            'Papua-New-Guinea',
                            'Timor-Leste',
                            'Burundi',	
                            'Tajikistan',	
                            'Curaçao',	
                            'Taiwan',	
                            'Aruba'	,
                            'Mauritius',	
                            'Andorra',				
                            'Mali',			
                            'Lesotho',			
                            'Congo'	,		
                            'Burkina-Faso',
                            'Nicaragua',	
                            'Djibouti',	
                            'Hong Kong',	
                            'South-Sudan',
                            'Equatorial-Guinea',
                            'Iceland',
                            'Channel-Islands',	
                            'CAR',	
                            'Saint-Lucia',
                            'Gambia',	
                            'Yemen',		
                            'Barbados',	
                            'Isle-of-Man',	
                            'New-Caledonia',	
                            'Brunei',	
                            'Eritrea',			
                            'Sierra-Leone',		
                            'Guinea-Bissau',
                            'Niger',		
                            'Liberia',		
                            'Gibraltar',	
                            'San-Marino',	
                            'Bermuda',		
                            'Chad',			
                            'Grenada',			
                            'Sint Maarten',	
                            'New-Zealand',
                            'Comoros',	
                            'Saint-Martin',	
                            'Liechtenstein',	
                            'St.-Vincent-Grenadines',	
                            'Sao-Tome-and-Principe',
                            'Monaco	',	
                            'Dominica',			
                            'Antigua-and-Barbuda',	
                            'Turks-and-Caicos',	
                            'British-Virgin-Islands',
                            'Bhutan',	
                            'Caribbean-Netherlands',	
                            'Saint-Kitts-and-Nevis',	
                            'St.-Barth',	
                            'Tanzania',	
                            'Faeroe-Islands',	
                            'Cayman-Islands',	
                            'Diamond-Princess',							
                            'Greenland',	
                            'Wallis-and-Futuna',	
                            'Anguilla',	
                            'Macao',
                            'Falkland-Islands',	
                            'Montserrat',	
                            'Saint-Pierre-Miquelon',
                            'Vatican-City',
                            'Solomon-Islands',	
                            'Western-Sahara',
                            'MS-Zaandam',	
                            'Palau',	
                            'Vanuatu',
                            'Marshall Islands',	
                            'Samoa'	,	
                            'Saint Helena',
                            'Micronesia')
    countrychoosen.grid(column = 5, row = 8)
    countrychoosen.current()


    submit_img = tk.PhotoImage(file="icon/submit_button.png")
    submit_img_size = submit_img.subsample(6,6)
    submit_button = tk.Button(root, image=submit_img_size, command= get_country_data)
    submit_button.grid(row=11,column=5)
    submit_button.config(borderwidth=0)
    submit_button.config(bg="#ffffff")
    submit_button.config(activebackground="#ffffff")


    root.mainloop()
