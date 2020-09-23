from tkinter.filedialog import askdirectory
from tkinter import Message,messagebox
from tkinter.messagebox import askquestion
from shutil import move
import os
import_file_path=None
export_file_path=None

def import_func():
    global import_file_path
    import_file_path=askdirectory()
def export_func():
    global export_file_path
    export_file_path=askdirectory()

def run_func():
    programming_extensions=[".asp",".py",".pl",".java",".sh",".swift",".vb",".php",".h",".cs",".class",".cgi",".c",".cpp"]
    audio_files=[".aif","cda","mid",".midi",".mp3",".mpa",".ogg",".wav",".wma",".wpl"]
    compressed_files=[".7z",".arj",".deb",".pkg",".rar",".rpm",".tar.gz",".z",".zip"]
    data_and_datbase_files=[".csv",".dat",".db",".dfb",".log",".mdb",".sav",".sql",".tar",".xml"]
    disk_and_media_files=[".bin",".dmg",".iso",".toast",".vcd"]
    email_file_extensions=[".email",".eml","emlx",".msg",".oft",".ost",".pst",".vcf"]
    executable_file_exetensions=[".apk",".bat",".bin",".cgi",".pl",".com",".exe",".gadget",".jar",".msi",".py",".wsf"]
    image_file_extensions=[".ai",".bmp",".gif",".ico",".jpeg",".png",".ps",".psd",".svg",".tif",".tiff"]
    font_file_extensions=[".fnt",".fon","otf","ttf"]
    Presentation_filee_formats=['.key',".odp",".pps",".ppt","pptx"]
    spreadsheet_file_extensions=[".ods",".xls",".xlsm",".xlsx"]
    system_related_file_formats=[".bak",".cab",".cfg",".cpl",".cur",".dll",".dmp",".drv",".icns",".ico",".ini",".lnk",".msi",".sys","sys",".tmp"]
    video_file_foramt_extensions=[".3g2",".3gp",".avi",".flv",".h264",".m4v",".mkv",".mov",".mp4",".mpg",".mpeg",".rm",".swf",".vob",".wmv"]
    word_processor_and_text_file_format_extensions=[".doc",".odt",".pdf",".rtf",".tex",".txt",".wpd"]

    list_of_items_in_import_directory=os.listdir(import_file_path)
    print(list_of_items_in_import_directory)
    Folders=["Audio files","Compressed files","Disc and media files","Data and database files","E-mail files","Executable files","Font files","Image files","Internet related files","Presentation files","Programming files","Spreadsheet files","System related files","Video Files","Word processor and text files"]
    for folder_name in Folders:
        if folder_name in list_of_items_in_import_directory:
            continue
        try:
            os.mkdir(export_file_path+"/"+folder_name)
        except:
            pass
    while True:
        if import_file_path == None:
            messagebox.showerror("Error","Please import a folder first!")
        break
    while True:
        if export_file_path==None:
            messagebox.showerror("Error","Export folder not detected!")
        break
#first extension 
    for item in list_of_items_in_import_directory:
        print(list_of_items_in_import_directory)
        for exten in programming_extensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Programming files")
            except:
                pass
#second extension
    for item in list_of_items_in_import_directory:
        for exten in audio_files:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Audio files")
            except:
                pass
    #third extension
    for item in list_of_items_in_import_directory:
        for exten in compressed_files:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Compressed files")
            except:
                pass
    #fourth extension
    for item in list_of_items_in_import_directory:
        for exten in data_and_datbase_files:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Data and database files")
            except:
                pass
    #5th extension
    for item in list_of_items_in_import_directory:
        for exten in disk_and_media_files:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Disc and media files")
            except:
                pass
    #6th extension
    for item in list_of_items_in_import_directory:
        for exten in email_file_extensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"E-mail files")
            except:
                pass
#7th extension
    for item in list_of_items_in_import_directory:
        for exten in executable_file_exetensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Executable files")
            except:
                pass

#8th extension
    for item in list_of_items_in_import_directory:
        for exten in image_file_extensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Image files")
            except:
                pass

#9th extension
    for item in list_of_items_in_import_directory:
        for exten in font_file_extensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Font files")
            except:
                pass

#10th extension
    for item in list_of_items_in_import_directory:
        for exten in Presentation_filee_formats:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Presentation files")
            except:
                pass

#11th extension
    for item in list_of_items_in_import_directory:
        for exten in spreadsheet_file_extensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Spreadsheet files")
            except:
                pass

#12th extension
    for item in list_of_items_in_import_directory:
        for exten in system_related_file_formats:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"System related files")
            except:
                pass

#13th extension
    for item in list_of_items_in_import_directory:
        for exten in video_file_foramt_extensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Video Files")
            except:
                pass
#14th extension
    for item in list_of_items_in_import_directory:
        for exten in word_processor_and_text_file_format_extensions:
            try:
                if item.count(exten)>0:
                    move(import_file_path+"/"+item,export_file_path+"/"+"Word processor and text files")
            except:
                pass
    ask_open_file=askquestion("Task has been completed","would you like open the folder?")
    if ask_open_file== "yes":
        stream=os.popen("start %windir%\explorer.exe " + export_file_path)
    if ask_open_file== "no":   
        exit()