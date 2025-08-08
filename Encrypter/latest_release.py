if True:
    if True:
        mt=''
        history=''
    if True: #import
        import time as t
        from PIL import Image as img
        from customtkinter import *
        import tkinter as tk_tkinter
        import datetime
        import os
    if True: #colors
        color1 = '#ffffff'
        color2 = '#242424'
        color3 = '#282828'
        color4 = '#323232'
        h_color = '#404040'
        color_active = '#555555'
        color_inactive = '#404040'
    if True: #dictionaries
        keyren_1 = {'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&',
                    'F': '*', 'G': '(','H': ')', 'I': '!', 'J': '^',
                    'K': '_', 'L': '+', 'M': '~', 'N': '`','O': '-',
                    'P': '=', 'Q': '{', 'R': '}', 'S': '[', 'T': ']',
                    'U': ';','V': ':', 'W': '"', 'X': "'", 'Y': '<',
                    'Z': '>', ' ': ' '}
        keyren_2 = dict(zip(keyren_1.values(), keyren_1.keys()))
        dictionary = keyren_1
    if True: #dictionary_text
        text1 = keyren_1
        text_after = '⟦ [k] ⋋/👁\⋌ [v] ⟧\n⟦ ———————-——————— ⟧\n'
        indentation = 0
        count = 0
        for i in range(len(text1) - 1):
            string = '⟦ '+(list(text1.keys()))[indentation] + '   ⋋/👁\⋌   ' + (list(text1.values()))[indentation]+' ⟧'
            count += 1
            if indentation != len(text1) - 2:
                string += '\n'
            text_after += string
            indentation += 1
    if True: #definitions
        def history_loop():
            global history
            history_window = CTk()
            history_window.title('History')
            def clear_history():
                history_log = ''
                open("Encrypter/source/log.txt", 'w').close()
                history_label.configure(text=history_log)
            def update_history():
                history_log = ''
                with open("Encrypter/source/log.txt",'r',encoding='utf-8') as f:
                    history_log = f.read()
                history_list = history_log.splitlines()
                index = 0
                history_log = ''
                for i in range(len(history_list)):
                    act = history_list[index]
                    history_log += '\n' + act
                    history_label.configure(text=history_log)
                    history_label.update()
                    t.sleep(0.1)
                    index += 1
            clear_button = CTkButton(history_window,command=clear_history,width=225,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,text='Clear history',font=('Cascadia Code',15))
            clear_button.place(x=15, y=627)
            with open("Encrypter/source/log.txt",'r',encoding='utf-8') as f:
                history_log = f.read()
            update_button = CTkButton(history_window,command=update_history,width=30,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,text='🗘',font=('Cascadia Code',15))
            update_button.place(x=255, y=627)
            history_window.iconbitmap("Encrypter/source/icons/history.ico")
            history_window.geometry('300x672+1225+150')
            history_title_label = CTkLabel(history_window,text='HISTORY',font=('Times New Roman',24),justify=CENTER)
            history_title_label.place(x=100,y=7.5)
            history_frame = CTkFrame(history_window,height = 573,width = 270)
            history_frame.place(x=15,y=39)
            history_label = CTkLabel(history_frame,text=history_log,font=('Cascadia Code',15),justify=LEFT)
            history_label.place(x=15,y=-14)
            history_window.mainloop()
        def animate_text(label, text, delay):
            for i in range(len(text) + 1):
                current_text = text[:i]
                label.configure(text=current_text)
                label.update()
                t.sleep(delay)
        def dict_open():
            not_main = CTk()
            not_main.geometry('225x672+470+150')
            not_main.title('Dictionary')
            not_main.iconbitmap("Encrypter/source/icons/dictionary.ico") 
            frame_not_main = CTkFrame(not_main,width=195,height=592)
            frame_not_main.place(x=15,y=65)
            label_not_main = CTkLabel(not_main,text='FREEMASONRY\nDICTIONARY',font = ('Times New Roman',24),width=200)
            label_not_main.place(x=15,y=6)
            label_not_main_1 = CTkLabel(frame_not_main,text=text_after,font=('Cascadia Code',15))
            label_not_main_1.place(x=15,y=15)
            not_main.mainloop()
        def action():
            first = input.get()
            key = list(first)
            print(key)
            number = 10 
            indx = 0;insert = '';insert_no_n = ''
            for i in range(len(key)):
                try:
                    if len(list(insert)) > number:
                        insert+='\n'
                        number+=number + 1
                    insert += dictionary.get(key[indx].capitalize())
                    insert_no_n += dictionary.get(key[indx].capitalize())
                except TypeError:pass
                indx+=1
            animate_text(output,insert,0.1)
            global history
            current_date = datetime.datetime.now()
            print(current_date)
            text=f'\n{current_date}'
            if dictionary == keyren_1:
                crypt = f'\nEncrypted '
            if dictionary == keyren_2:
                crypt = f'\nDecrypted '
            text=text+crypt+'"'+first+'"'+'\ninto '+insert_no_n+'\n'
            history += text
            print(history)
            with open("Encrypter/source/log.txt",'a',encoding='utf-8') as f:
                f.write(text)
        def dictionary_change():
            global dictionary
            if dictionary == keyren_1:
                dictionary = keyren_2
                change_button.configure(text='Decrypting')
            elif dictionary == keyren_2:
                dictionary = keyren_1
                change_button.configure(text='Encrypting')
        def keyboard_loop():
            def command_q():
                input.insert(END,keyren_1.get('Q'))
            def command_w():
                input.insert(END,keyren_1.get('W'))
            def command_e():
                input.insert(END,keyren_1.get('E'))
            def command_r():
                input.insert(END,keyren_1.get('R'))
            def command_t():
                input.insert(END,keyren_1.get('T'))
            def command_y():
                input.insert(END,keyren_1.get('Y'))
            def command_u():
                input.insert(END,keyren_1.get('U'))
            def command_i():
                input.insert(END,keyren_1.get('I'))
            def command_o():
                input.insert(END,keyren_1.get('O'))
            def command_p():
                input.insert(END,keyren_1.get('P'))
            def command_a():
                input.insert(END,keyren_1.get('A'))
            def command_s():
                input.insert(END,keyren_1.get('S'))
            def command_d():
                input.insert(END,keyren_1.get('D'))
            def command_f():
                input.insert(END,keyren_1.get('F'))
            def command_g():
                input.insert(END,keyren_1.get('G'))
            def command_h():
                input.insert(END,keyren_1.get('H'))
            def command_j():
                input.insert(END,keyren_1.get('J'))
            def command_k():
                input.insert(END,keyren_1.get('K'))
            def command_l():
                input.insert(END,keyren_1.get('L'))
            def command_z():
                input.insert(END,keyren_1.get('Z'))
            def command_x():
                input.insert(END,keyren_1.get('X'))
            def command_c():
                input.insert(END,keyren_1.get('C'))
            def command_v():
                input.insert(END,keyren_1.get('V'))
            def command_b():
                input.insert(END,keyren_1.get('B'))
            def command_n():
                input.insert(END,keyren_1.get('N'))
            def command_m():
                input.insert(END,keyren_1.get('M'))
            def command__():
                input.insert(END,' ')
            if True: #buttons
                #row1
                keyboard = CTk()
                keyboard.title('Keyboard')
                keyboard.iconbitmap("Encrypter/source/icons/keyboard.ico")
                keyboard.geometry('500x270+710+552')
                keyboard_window = CTkFrame(keyboard,width=470,height=240,fg_color=color3)
                keyboard_window.place(x=15,y=15)
                button_q = CTkButton(keyboard_window,command=command_q,text='q',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#1
                button_w = CTkButton(keyboard_window,command=command_w,text='w',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#2
                button_e = CTkButton(keyboard_window,command=command_e,text='e',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#3
                button_r = CTkButton(keyboard_window,command=command_r,text='r',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#4
                button_t = CTkButton(keyboard_window,command=command_t,text='t',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#5
                button_y = CTkButton(keyboard_window,command=command_y,text='y',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#6
                button_u = CTkButton(keyboard_window,command=command_u,text='u',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#1
                button_i = CTkButton(keyboard_window,command=command_i,text='i',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#2
                button_o = CTkButton(keyboard_window,command=command_o,text='o',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#3
                button_p = CTkButton(keyboard_window,command=command_p,text='p',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#4
                button_a = CTkButton(keyboard_window,command=command_a,text='a',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#5
                button_s = CTkButton(keyboard_window,command=command_s,text='s',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#1
                button_d = CTkButton(keyboard_window,command=command_d,text='d',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#2
                button_f = CTkButton(keyboard_window,command=command_f,text='f',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#3
                button_g = CTkButton(keyboard_window,command=command_g,text='g',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#4
                button_h = CTkButton(keyboard_window,command=command_h,text='h',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#5
                button_j = CTkButton(keyboard_window,command=command_j,text='j',width=60,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#6
                button_k = CTkButton(keyboard_window,command=command_k,text='k',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#1
                button_l = CTkButton(keyboard_window,command=command_l,text='l',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#2
                button_z = CTkButton(keyboard_window,command=command_z,text='z',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#3
                button_x = CTkButton(keyboard_window,command=command_x,text='x',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#4
                button_c = CTkButton(keyboard_window,command=command_c,text='c',width=76,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#5
                button_v = CTkButton(keyboard_window,command=command_v,text='v',width=55,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#1
                button_b = CTkButton(keyboard_window,command=command_b,text='b',width=55,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#2
                button__ = CTkButton(keyboard_window,command=command__,text='Space',width=160,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#пробел
                button_n = CTkButton(keyboard_window,command=command_n,text='n',width=55,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#4
                button_m = CTkButton(keyboard_window,command=command_m,text='m',width=55,height=30,bg_color='#282828',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))#5
                button_q.place(x=15,y=15)
                button_w.place(x=91,y=15)
                button_e.place(x=167,y=15)
                button_r.place(x=243,y=15)
                button_t.place(x=319,y=15)
                button_y.place(x=395,y=15)
                button_u.place(x=15,y=60)
                button_i.place(x=106,y=60)
                button_o.place(x=197,y=60)
                button_p.place(x=288,y=60)
                button_a.place(x=379,y=60)
                button_s.place(x=15,y=105)
                button_d.place(x=91,y=105)
                button_f.place(x=167,y=105)
                button_g.place(x=243,y=105)
                button_h.place(x=319,y=105)
                button_j.place(x=395,y=105)
                button_k.place(x=15,y=150)
                button_l.place(x=106,y=150)
                button_z.place(x=197,y=150)
                button_x.place(x=288,y=150)
                button_c.place(x=379,y=150)
                button_v.place(x=15,y=195)
                button_b.place(x=85,y=195)
                button_n.place(x=330,y=195)
                button_m.place(x=400,y=195)
                button__.place(x=155,y=195)
                keyboard.mainloop()
    if True: #build windows
        main = CTk()
        main.title('Encrypter')
        main.geometry('500x357+710+150')
        main.iconbitmap("Encrypter/source/icons/file.ico") 
    if True: #frames
        frame1 = CTkFrame(main,width=470,height=327,fg_color=color3)
        frame1.place(x=15,y=15) # this one frame that is the biggest
        if True: #image
            path = "Encrypter/source/images/dark.png"
            pil_image = img.open(path)
            ctk_image = CTkImage(pil_image,size=(150,187))
            image_place = CTkLabel(frame1,text='',image=ctk_image)
            image_place.place(x=15,y=15)
        frame2 = CTkFrame(frame1,width = 277, height = 187,fg_color=color4)
        frame2.place(x=180,y=15)
        frame3 = CTkFrame(frame1,width = 310, height = 50,fg_color=color4)
        frame3.place(x=15,y=217)
        frame4_1 = CTkFrame(frame1, width=115, height=50,fg_color=color4)
        frame4_1.place(x=340,y=217)
    if True: #labels and entries
        input = CTkEntry(frame3,width=280,height=20,font = ('Times New Roman',18),placeholder_text='Input',border_color=color4,fg_color='#323232')
        input.place(x=10,y=12.5)
        output = CTkLabel(frame2,width=247,height=157,font = ('Times New Roman',24),text='')
        output.place(x=15,y=15)
    if True: #buttons
        action_button = CTkButton(frame1,command=action,width=120,height=30,text='Action',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))
        action_button.place(x=15,y=282)
        dictionary_button = CTkButton(frame1,command=dict_open,width=120,height=30,text='Dictionary',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))
        dictionary_button.place(x=150,y=282)
        change_button = CTkButton(frame4_1,bg_color='#282828',command=dictionary_change,width=115,height=50,text='Encrypting',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))
        change_button.place(x=0,y=0)
        history_button = CTkButton(frame1,bg_color='#282828',command=history_loop,width=35,height=30,text='🗎',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',16))
        history_button.place(x=420,y=282)
        keyboard_button = CTkButton(frame1,bg_color='#282828',command=keyboard_loop,width=120,height=30,text='Keyboard',text_color=color1,fg_color=color4,hover_color=h_color,font=('Cascadia Code',15))
        keyboard_button.place(x=285,y=282)
    if True: #mainloop#
        main.mainloop()