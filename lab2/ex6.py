import numpy as np
import matplotlib.pyplot as plt


def signals(freq, time):
    a_sig = np.sin(2 * np.pi * (freq/2) * time)
    b_sig = np.sin(2 * np.pi * (freq/4) * time)
    c_sig = np.sin(2 * np.pi * 0 * time)
    return (a_sig, b_sig, c_sig)


t = np.arange(0, 1, step=1/1600)
(a_sig_arange, b_sig_arange, c_sig_arange) = signals(1600,t)

fig, ass = plt.subplots(3)
fig.suptitle('Frecvente fundamentale')

ass[0].plot(t,a_sig_arange)
ass[0].set_title('fs/2')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')

ass[1].plot(t,b_sig_arange)
ass[1].set_title('fs/4')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')

ass[2].plot(t,c_sig_arange)
ass[2].set_title('0 Hz')
ass[2].set_xlabel('time')
ass[2].set_ylabel('amplitude')

plt.savefig("ex6-arange.pdf", format="pdf", bbox_inches="tight")
plt.show()


t_lin = np.linspace(0, 1, 1600)
(a_sig_lin, b_sig_lin, c_sig_lin) = signals(1600,t_lin)

fig, ass = plt.subplots(3)
fig.suptitle('Frecvente fundamentale')

ass[0].plot(t_lin,a_sig_lin)
ass[0].set_title('fs/2')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')

ass[1].plot(t_lin,b_sig_lin)
ass[1].set_title('fs/4')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')

ass[2].plot(t_lin,c_sig_lin)
ass[2].set_title('0 Hz')
ass[2].set_xlabel('time')
ass[2].set_ylabel('amplitude')

plt.savefig("ex6-linspace.pdf", format="pdf", bbox_inches="tight")
plt.show()

# In urma unor teste am observat niste diferente legate de semnalul cu frecventa fundamentala = frecventa de esantionare / 2
# In teorie acesta ar trebui sa fie liniar pe 0 conform calculului sin(2π * (fs/2) * n * 1/fs) = sin(nπ) = 0
# Din pacate niciunul dintre semnalele fs/2 generate pentru frecventa de esantionare 1/1600 nu a putut ilustra aceasta realitate din cauza limitarilor calculelor cu numere franctionare
# (cum a fost de alt fel demonstrat la laboratorul de calcul numeric)
# Dar de aici deviem in contiunare in doua cazuri, in functie de ce functie folosim sa facem esantioanele:
#   - np.arange(start,stop,step) returneaza un vector de esantioane de distanta egala cu step excluzand stop
#   - np.linspace(start,stop,num) returneaza un vector de num esantioane incluzand stop, ceea ce decaleaza esantioanele, afectand frecventa de esantionare
# Astfel arange are un rezultat mai apropiat de rezultatul teoretic, dar nu exact (e^-13)
# Incercam sa simulam

t_sim = np.arange(0,1,1/1600)
(a_sig_sim, b_sig_sim, c_sig_sim) = np.round(signals(1600,t_sim),11)

fig, ass = plt.subplots(3)
fig.suptitle('Frecvente fundamentale')

ass[0].plot(t_sim,a_sig_sim)
ass[0].set_title('fs/2')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')

ass[1].plot(t_sim,b_sig_sim)
ass[1].set_title('fs/4')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')

ass[2].plot(t_sim,c_sig_sim)
ass[2].set_title('0 Hz')
ass[2].set_xlabel('time')
ass[2].set_ylabel('amplitude')

plt.savefig("ex6-simulation.pdf", format="pdf", bbox_inches="tight")
plt.show()


# Am simulat un semnal liniar 0 pentru fs/2 prin folosirea functiei round care elimina "zgomotul" generat de erorile de precizie
# Pana si np.sin(np.pi) are o eroare de 1.2246467991473532e-16 care se propaga mai departe in calcule
