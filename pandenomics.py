# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")
#from dataprep.eda import plot, plot_correlation, create_report, plot_missing
from matplotlib import font_manager, rc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

dataset1 = pd.read_csv("메르스전후_강남구.csv", encoding='cp949')
dataset2 = pd.read_csv("메르스전후_마포구.csv", encoding='cp949')
dataset3 = pd.read_csv("메르스전후_용산구.csv", encoding='cp949')
dataset4 = pd.read_csv("코로나전후_강남구.csv", encoding='cp949')
dataset5 = pd.read_csv("코로나전후_마포구.csv", encoding='cp949')
dataset6 = pd.read_csv("코로나전후_용산구.csv", encoding='cp949')

subdata1_1 = dataset1[(dataset1.상권_구분_코드_명 == "골목상권")]
subdata1_2 = dataset1[(dataset1.상권_구분_코드_명 == "발달상권")]
subdata1_3 = dataset1[(dataset1.상권_구분_코드_명 == "관광특구")]
subdata2_1 = dataset2[(dataset2.상권_구분_코드_명 == "골목상권")]
subdata2_2 = dataset2[(dataset2.상권_구분_코드_명 == "발달상권")]
subdata3_1 = dataset3[(dataset3.상권_구분_코드_명 == "골목상권")]
subdata3_2 = dataset3[(dataset3.상권_구분_코드_명 == "발달상권")]
subdata3_3 = dataset3[(dataset3.상권_구분_코드_명 == "관광특구")]
subdata4_1 = dataset4[(dataset4.상권_구분_코드_명 == "골목상권")]
subdata4_2 = dataset4[(dataset4.상권_구분_코드_명 == "발달상권")]
subdata4_3 = dataset4[(dataset4.상권_구분_코드_명 == "관광특구")]
subdata5_1 = dataset5[(dataset5.상권_구분_코드_명 == "골목상권")]
subdata5_2 = dataset5[(dataset5.상권_구분_코드_명 == "발달상권")]
subdata6_1 = dataset6[(dataset6.상권_구분_코드_명 == "골목상권")]
subdata6_2 = dataset6[(dataset6.상권_구분_코드_명 == "발달상권")]
subdata6_3 = dataset6[(dataset6.상권_구분_코드_명 == "관광특구")]

try:
    from tkinter import *
except:
    from Tkinter import *

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self._text1 = None
        self._text2 = None
        self.switch_frame(Start)
        self.title("펜데노믹스 벤쳐")
        self.geometry("1024x720")
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    def set_text1(self, text):
        self._text1 = text
    
    def set_text2(self, text):
        self._text2 = text

class Start(Frame):
     def __init__(self, master):
        Frame.__init__(self, master)
        txt1=Label(self,text="최고의 창업종목을 추천합니다!",font=('Yu Gothic', 30,'normal','bold'),fg = "purple").pack()
        btn1 = Button(self, width = 11,height=1,font=('Yu Gothic', 14,'normal','bold'), text ="시작" ,
                      command=lambda: (master.switch_frame(StartPage), master.set_text1("시작"))).pack(side="bottom",anchor="c")
        img=PhotoImage(file="배경화면.gif") #####
        my_label=Label(self,image=img)
        my_label.image=img
        my_label.pack()
        
class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        txt1=Label(self,text="원하시는 자치구를 선택하세요.", font=('Helvetica', 30, "bold")).pack()
        Button(self, width=11, height=1, font=('Yu Gothic', 14,'normal','bold'), text="용산구",
                  command=lambda: (master.switch_frame(PageOne), master.set_text1("용산구"))).pack(side="bottom",anchor="c")
        Button(self,  width=11, height=1, font=('Yu Gothic', 14,'normal','bold'),text="마포구",
                  command=lambda: (master.switch_frame(PageOne), master.set_text1("마포구"))).pack(side="bottom",anchor="c")
        Button(self, width=11, height=1, font=('Yu Gothic', 14,'normal','bold'), text="강남구",
                  command=lambda: (master.switch_frame(PageOne), master.set_text1("강남구"))).pack(side="bottom",anchor="c")
        img=PhotoImage(file="seoul_map.gif") #####
        lbl = Label(self,image = img)
        lbl.image = img
        lbl.pack()

class PageOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="원하시는 상권을 선택하세요.", font=('Helvetica', 30, "bold")).pack()
        Button(self, width=11, height=1, font=('Yu Gothic', 14,'normal','bold'), text="관광특구",
                  command=lambda: (master.switch_frame(PageTwo), master.set_text2("관광특구"))).pack(side="bottom",anchor="c")
        Button(self, width=11, height=1, font=('Yu Gothic', 14,'normal','bold'), text="발달상권",
                  command=lambda: (master.switch_frame(PageTwo), master.set_text2("발달상권"))).pack(side="bottom",anchor="c")
        Button(self, width=11, height=1, font=('Yu Gothic', 14,'normal','bold'), text="골목상권",
                  command=lambda: (master.switch_frame(PageTwo), master.set_text2("골목상권"))).pack(side="bottom",anchor="c")
        img=PhotoImage(file="상권.gif") #####
        lbl = Label(self,image = img)
        lbl.image = img
        lbl.pack()
        
class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.__init__(self, master)
        Label(self, text="둘 중 하나 선택하세요.", font=('Helvetica', 18, "bold")).pack(side="top", padx = 385, pady=206)
        Frame.configure(self,bg='white')
        Button(self,  width=11, height=1, font=('Yu Gothic', 14,'normal','bold'),text="처음으로",
                  command=lambda: master.switch_frame(StartPage)).pack(side="bottom",anchor="c")
        Button(self, width=11, height=1, font=('Yu Gothic', 14,'normal','bold'), text="그래프 탐색",
                  command=lambda: master.switch_frame(PageThree)).pack(side="bottom",anchor="c")
        Button(self, width=11, height=1, font=('Yu Gothic', 14,'normal','bold'), text="Top3",
                  command=lambda: master.switch_frame(PageFour),).pack(side="bottom",anchor="c")
        
        
class PageThree(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        if(master._text1 == "강남구") & (master._text2 == "골목상권"):
            selecteddata = subdata1_1
            selecteddata2 = subdata4_1
            img1 = PhotoImage(file='강남구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text= "업종 목록 \nPC방, 가구, 가방, 가전제품, 가전제품수리, 고시원, 골프연습장\n, 네일숍, 노래방, 당구장, 문구, 미곡판매, 미용실, 반찬가게\n, 분식전문점, 부동산중개업, 서적, 섬유제품, 세탁소, 수산물판매, 슈퍼마켓\n, 스포츠 강습, 스포츠클럽, 시계및귀금속, 신발, 안경, 애완동물, 양식음식점\n, 여관, 예술학원, 완구, 외국어학원, 운동/경기용품, 육류판매, 의료기기\n, 의약품, 인테리어, 일반교습학원, 일반의류, 일반의원, 일식음식점, 자동차미용\n, 자동차수리, 자전거 및 기타운송장비, 전자상거래업, 제과점, 조명용품, 중식음식점, 철물점\n, 청과상, 치과의원, 치킨전문점, 커피-음료, 컴퓨터및주변장치판매, 패스트푸드점, 편의점\n, 피부관리실, 한식음식점, 한의원, 핸드폰, 호프-간이주점, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side = "top", padx = 10, pady=32)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("강남구 골목상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
            
            def make_plot2(s):
                root = Tk()
                root.title("강남구 골목상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
           
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
                  
            Button(self,  width=15, height=1, font=('Yu Gothic', 14,'normal','bold'),text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
                        
        if(master._text1 == "강남구") & (master._text2 == "발달상권"):
            selecteddata = subdata1_2
            selecteddata2 = subdata4_2
            img1 = PhotoImage(file='강남구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack()
            Label(self, text=  "업종 목록 \nPC방, 가구, 가방, 가전제품, 가전제품수리, 고시원, 골프연습장\n, 네일숍, 노래방, 당구장, 문구, 미곡판매, 미용실, 반찬가게\n, 분식전문점, 부동산중개업, 서적, 섬유제품, 세탁소, 수산물판매, 슈퍼마켓\n, 스포츠 강습, 스포츠클럽, 시계및귀금속, 신발, 안경, 애완동물, 양식음식점\n, 여관, 예술학원, 완구, 외국어학원, 운동/경기용품, 육류판매, 의료기기\n, 의약품, 인테리어, 일반교습학원, 일반의류, 일반의원, 일식음식점, 자동차미용\n, 자동차수리, 자전거 및 기타운송장비, 전자상거래업, 제과점, 조명용품, 중식음식점, 철물점\n, 청과상, 치과의원, 치킨전문점, 커피-음료, 컴퓨터및주변장치판매, 패스트푸드점, 편의점\n, 피부관리실, 한식음식점, 한의원, 핸드폰, 호프-간이주점, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side="top", padx = 10, pady=32)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("강남구 발달상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
           
            def make_plot2(s):
                root = Tk()
                root.title("강남구 발달상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
                  
            Button(self,  width=15, height=1, font=('Yu Gothic', 14,'normal','bold'),text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
                  
            Button(self,  width=15, height=1, font=('Yu Gothic', 14,'normal','bold'),text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
                  
        if(master._text1 == "강남구") & (master._text2 == "관광특구"):
            selecteddata = subdata1_3
            selecteddata2 = subdata4_3
            img1 = PhotoImage(file='강남구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text= "업종 목록\n가구, 가방, 가전제품, 네일숍, 문구, 미용실, 반찬가게, 분식전문점\n, 섬유제품, 슈퍼마켓, 스포츠클럽, 시계및귀금속, 신발, 안경, 양식음식점\n, 완구, 운동/경기용품, 의약품, 인테리어, 일반의류, 일반의원, 일식음식점\n, 전자상거래업, 제과점, 중식음식점, 치과의원, 커피-음료, 컴퓨터및주변장치판매, 패스트푸드점\n, 편의점, 피부관리실, 한식음식점, 핸드폰, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side="top", padx = 40, pady=70)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("강남구 관광특구 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
           
            def make_plot2(s):
                root = Tk()
                root.title("강남구 관광특구 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
                  
            Button(self,  width=15, height=1, font=('Yu Gothic', 14,'normal','bold'),text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
                  
        if(master._text1 == "마포구") & (master._text2 == "골목상권"):
            selecteddata = subdata2_1
            selecteddata2 = subdata5_1
            img1 = PhotoImage(file='마포구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text= "업종 목록\nPC방, 가구, 가방, 가전제품, 가전제품수리, 골프연습장, 네일숍\n, 노래방, 당구장, 문구, 미곡판매, 미용실, 반찬가게, 분식전문점\n, 서적, 섬유제품, 세탁소, 수산물판매, 슈퍼마켓, 스포츠 강습, 스포츠클럽\n, 시계및귀금속, 신발, 안경, 애완동물, 양식음식점, 여관, 예술학원\n, 완구, 외국어학원, 운동/경기용품, 육류판매, 의료기기, 의약품, 인테리어\n, 일반교습학원, 일반의류, 일반의원, 일식음식점, 자동차미용, 자동차수리, 자전거 및 기타운송장비\n, 전자상거래업, 제과점, 조명용품, 중식음식점, 철물점, 청과상, 치과의원\n, 치킨전문점, 커피-음료, 컴퓨터및주변장치판매, 패스트푸드점, 편의점, 피부관리실, 한식음식점\n, 한의원, 핸드폰, 호프-간이주점, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side="top", padx = 10, pady=32)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("마포구 골목상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
           
            def make_plot2(s):
                root = Tk()
                root.title("마포구 골목상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
                  
        if(master._text1 == "마포구") & (master._text2 == "발달상권"):
            selecteddata = subdata2_2
            selecteddata2 = subdata5_2
            img1 = PhotoImage(file='마포구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text= "업종 목록\nPC방, 가구, 가방, 가전제품, 가전제품수리, 골프연습장, 네일숍\n, 노래방, 당구장, 문구, 미곡판매, 미용실, 반찬가게, 분식전문점\n, 부동산중개업, 서적, 섬유제품, 세탁소, 수산물판매, 슈퍼마켓, 스포츠 강습, 스포츠클럽\n, 시계및귀금속, 신발, 안경, 애완동물, 양식음식점, 여관, 예술학원\n, 완구, 외국어학원, 운동/경기용품, 육류판매, 의료기기, 의약품, 인테리어\n, 일반교습학원, 일반의류, 일반의원, 일식음식점, 자동차미용, 전자상거래업, 제과점, 조명용품, 중식음식점, 철물점, 치과의원\n, 치킨전문점, 커피-음료, 컴퓨터및주변장치판매, 패스트푸드점, 편의점, 피부관리실, 한식음식점\n, 한의원, 핸드폰, 호프-간이주점, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side="top", padx = 10, pady=42)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("마포구 발달상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                plt.ticklabel_format(style='plain', axis='y')
                root.mainloop()
           
            def make_plot2(s):
                root = Tk()
                root.title("마포구 발달상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                plt.ticklabel_format(style='plain', axis='y')
                root.mainloop()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
                  
        
        if(master._text1 == "마포구") & (master._text2 == "관광특구"):
            img1 = PhotoImage(file='마포구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text= "데이터가 없습니다.", font=('Helvetica', 18, "bold")).pack(side="top", padx = 10, pady=120)               
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack(side="bottom",anchor="c")
            
        if(master._text1 == "용산구") & (master._text2 == "골목상권"):
            selecteddata = subdata3_1
            selecteddata2 = subdata6_2
            img1 = PhotoImage(file='용산구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text= "업종 목록\nPC방, 가구, 가방, 가전제품, 가전제품수리, 골프연습장, 네일숍\n, 노래방, 당구장, 문구, 미곡판매, 미용실, 반찬가게, 분식전문점\n, 서적, 섬유제품, 세탁소, 수산물판매, 슈퍼마켓, 스포츠 강습, 스포츠클럽\n, 시계및귀금속, 신발, 안경, 애완동물, 양식음식점, 여관, 예술학원\n, 외국어학원, 운동/경기용품, 육류판매, 의료기기, 의약품, 인테리어, 일반교습학원\n, 일반의류, 일반의원, 일식음식점, 자동차미용, 자동차수리, 자전거 및 기타운송장비, 전자상거래업\n, 제과점, 조명용품, 중식음식점, 철물점, 청과상, 치과의원, 치킨전문점\n, 커피-음료, 컴퓨터및주변장치판매, 패스트푸드점, 편의점, 피부관리실, 한식음식점\n, 한의원, 핸드폰, 호프-간이주점, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side="top", padx = 10, pady=32)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("용산구 골목상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
           
            def make_plot2(s):
                root = Tk()
                root.title("용산구 골목상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
                  
        if(master._text1 == "용산구") & (master._text2 == "발달상권"):
            selecteddata = subdata3_2
            selecteddata2 = subdata6_2
            img1 = PhotoImage(file='용산구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text=  "업종 목록\nPC방, 가구, 가방, 가전제품, 가전제품수리, 골프연습장, 네일숍\n, 노래방, 당구장, 문구, 미용실, 반찬가게, 분식전문점, 서적\n, 수산물판매, 슈퍼마켓, 스포츠 강습, 스포츠클럽, 시계및귀금속, 신발, 안경\n, 애완동물, 양식음식점, 여관, 예술학원, 완구, 운동/경기용품, 의료기기\n, 의약품, 인테리어, 일반교습학원, 일반의류, 일반의원, 일식음식점, 자동차미용\n, 자동차수리, 자전거 및 기타운송장비, 전자상거래업, 제과점, 조명용품, 중식음식점, 철물점\n, 치과의원, 치킨전문점, 커피-음료, 컴퓨터및주변장치판매, 패스트푸드점, 편의점, 피부관리실\n, 한식음식점, 한의원, 핸드폰, 호프-간이주점, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side="top", padx = 10, pady=42)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("용산구 발달상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
           
            def make_plot2(s):
                root = Tk()
                root.title("용산구 발달상권 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
                  
        if(master._text1 == "용산구") & (master._text2 == "관광특구"):
            selecteddata = subdata3_3
            selecteddata2 = subdata6_3
            img1 = PhotoImage(file='용산구_행정동1.gif') #####
            lbl = Label(self,image = img1)
            lbl.image = img1
            lbl.pack(side="top")
            Label(self, text= "업종 목록\n가구, 가방, 가전제품수리, 골프연습장, 네일숍, 노래방, 당구장\n, 문구, 미용실, 반찬가게, 분식전문점, 서적, 섬유제품, 세탁소\n, 슈퍼마켓, 스포츠클럽, 시계및귀금속, 신발, 안경, 애완동물, 양식음식점\n, 여관, 예술학원, 운동/경기용품, 육류판매, 의료기기, 의약품, 일반의류\n, 일반의원, 일식음식점, 자동차미용, 전자상거래업, 제과점, 조명용품, 중식음식점\n, 치과의원, 치킨전문점, 커피-음료, 패스트푸드점, 편의점, 피부관리실, 한식음식점\n, 한의원, 핸드폰, 호프-간이주점, 화장품, 화초", font=('Helvetica', 12, "bold")).pack(side="top", padx = 10, pady=51)
            ent1 = Entry(self)
            ent1.pack()
                     
            def make_plot1(s):
                root = Tk()
                root.title("용산구 관광특구 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata[(selecteddata.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
           
            def make_plot2(s):
                root = Tk()
                root.title("용산구 관광특구 매출추이")
                figure2 = plt.figure(figsize=(10,6))
                ax2 = figure2.add_subplot(111)
                line2 = FigureCanvasTkAgg(figure2,root)
                line2.get_tk_widget().pack()
                subdata = selecteddata2[(selecteddata2.서비스_업종_코드_명 == s)]
                subdata.groupby('기준_분기_코드')['점포당매출'].mean().plot()
                plt.ticklabel_format(style='plain', axis='y')
                plt.ylabel('분기별 평균매출')
                plt.xlabel('년도별 분기')
                root.mainloop()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '메르스 그래프 보기',
                            command=lambda: make_plot1(str(ent1.get()))).pack()
            
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '코로나 그래프 보기',
                            command=lambda: make_plot2(str(ent1.get()))).pack()
                  
            Button(self, width=15, height=1, font=('Yu Gothic', 14,'normal','bold'), text= '뒤로가기',
                            command=lambda: master.switch_frame(PageTwo)).pack()
    
class PageFour(Frame): ##top3
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='white')
        photo1 = PhotoImage(file="강남구.gif")
        photo2 = PhotoImage(file="용산구1.gif")
        photo3 = PhotoImage(file="마포구1.gif")
        fbtn1 = Button(self, image=photo1)
        fbtn2 = Button(self, image=photo2)
        fbtn3 = Button(self, image=photo3)
        fbtn1.image=photo1
        fbtn2.image=photo2
        fbtn3.image=photo3
        if(master._text1 == "강남구") & (master._text2 == "발달상권"):
            Label(self, text= "1.애완동물", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top", padx = 400, pady=10)
            Label(self, text= "2.일반의원", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top", padx = 400, pady=10)
            Label(self, text= "3.편의점", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top", padx = 400, pady=10)##text에 업종 나열
            fbtn1.pack(padx=10,pady=112)
        if(master._text1 == "강남구") & (master._text2 == "관광특구"):
            Label(self, text= "1.의약품", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top",  padx = 400, pady=10)
            Label(self, text= "2.핸드폰", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top",  padx = 400, pady=10)
            Label(self, text= "3.치과의원", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top",  padx = 400, pady=10)##text에 업종 나열
            fbtn1.pack(padx=10,pady=112)
        if(master._text1 == "강남구") & (master._text2 == "골목상권"):
            Label(self, text= "1.일반의원", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top",  padx = 400, pady=10)
            Label(self, text= "2.화초", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top",  padx = 400, pady=10)
            Label(self, text= "3.완구", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top",  padx = 400, pady=10)
            fbtn1.pack(padx=10,pady=112)
            
        if(master._text1 == "마포구") & (master._text2 == "골목상권"):
            Label(self, text= "1.문구", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top", padx = 400, pady=10)
            Label(self, text= "2.의료기기", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top", padx = 400, pady=10)
            Label(self, text= "3.편의점", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top", padx = 400, pady=10)
            fbtn3.pack(padx=10,pady=112)
        if(master._text1 == "마포구") & (master._text2 == "발달상권"):
            Label(self, text= "1.여관", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top", padx = 400, pady=10)
            Label(self, text= "2.수산물판매", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top", padx = 400, pady=10)
            Label(self, text= "3.가구", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top", padx = 400, pady=10)
            fbtn3.pack(padx=10,pady=112)
        if(master._text1 == "마포구") & (master._text2 == "관광특구"):
            Label(self, text= "데이터가 없습니다", font=('Helvetica', 18, "bold","italic"),bg="white").pack(side="top", padx = 400, pady=200)
       
        if(master._text1 == "용산구") & (master._text2 == "골목상권"):
            Label(self, text= "1.자동차 수리", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top", padx = 400, pady=10)
            Label(self, text= "2.육류판매", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top", padx = 400, pady=10)
            Label(self, text= "3.당구장", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top", padx = 400, pady=10)
            fbtn2.pack(padx=10,pady=124)
        if(master._text1 == "용산구") & (master._text2 == "발달상권"):
            Label(self, text= "1.세탁소", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top", padx = 400, pady=10)
            Label(self, text= "2.섬유제품", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top", padx = 400, pady=10)
            Label(self, text= "3.서적", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top", padx = 400, pady=10)
            fbtn2.pack(padx=10,pady=124)
        if(master._text1 == "용산구") & (master._text2 == "관광특구"):
            Label(self, text= "1.수산물판매", font=('Helvetica', 18, "bold","italic"),bg="gold").pack(side="top", padx = 400, pady=10)
            Label(self, text= "2.가구", font=('Helvetica', 18, "bold","italic"),bg="silver").pack(side="top", padx = 400, pady=10)
            Label(self, text= "3.자동차 수리", font=('Helvetica', 18, "bold","italic"),bg="brown").pack(side="top", padx = 400, pady=10)
            fbtn2.pack(padx=10,pady=124)
        Button(self, text="뒤로가기",width=11, height=1, font=('Yu Gothic', 14,'normal','bold'),
                    command=lambda: master.switch_frame(PageTwo)).pack()
        
class PageFive(Frame): ## 그래프 보기
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='purple')
        Label(self, text="여기에 그래프 넣기", font=('Helvetica', 18, "bold")).pack(side="top", padx = 385, pady=277)
        Button(self, text="뒤로가기",width=11, height=1, font=('Yu Gothic', 14,'normal','bold'),
                  command=lambda: master.switch_frame(PageThree)).pack()
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
