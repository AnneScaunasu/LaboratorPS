import numpy as np
import matplotlib.pyplot as plt


def reconstruct_original_signal_in_t(sig, t_vals, sample_times, ts):
    return np.array([np.sum(sig * np.sinc((ti - sample_times)/ts)) for ti in t_vals])


# a
t = np.arange(-3, 3, 0.0001)
B = 1
x = np.pow(np.sinc(B * t), 2)

plt.plot(t,x)
plt.axhline(0, color='black', linewidth=0.7)
plt.title("sinc^2(Bt)")
plt.savefig(f"ex1a.pdf", format="pdf", bbox_inches="tight")
plt.show()

# b
ts1 = 1
t1 = np.arange(-3, 3, ts1)
sig_1 =np.pow(np.sinc(B * t1), 2)
new_sig_1 = reconstruct_original_signal_in_t(sig_1, t, t1, ts1)

ts1_5 = 1/1.5
t1_5 = np.arange(-3, 3, 1/1.5)
sig_1_5 = np.pow(np.sinc(B * t1_5), 2)
new_sig_1_5 = reconstruct_original_signal_in_t(sig_1_5, t, t1_5, ts1_5)

ts2 = 0.5
t2 = np.arange(-3, 3, 0.5)
sig_2 = np.pow(np.sinc(B * t2), 2)
new_sig_2 = reconstruct_original_signal_in_t(sig_2, t, t2, ts2)

ts4 = 0.25
t4 = np.arange(-3, 3, 0.25)
sig_4 = np.pow(np.sinc(B * t4), 2)
new_sig_4 = reconstruct_original_signal_in_t(sig_4, t, t4, ts4)

fig, ass = plt.subplots(2,2)

ass[0,0].plot(t,new_sig_1,color="lime",linestyle="dashed")
ass[0,0].stem(t1, sig_1, linefmt="orange", markerfmt="orange", basefmt="orange")
ass[0,0].axhline(0, color='black', linewidth=0.7)

ass[0,1].plot(t,new_sig_1_5,color="lime",linestyle="dashed")
ass[0,1].stem(t1_5, sig_1_5, linefmt="orange", markerfmt="orange", basefmt="orange")
ass[0,1].axhline(0, color='black', linewidth=0.7)


ass[1,0].plot(t,new_sig_2,color="lime",linestyle="dashed")
ass[1,0].stem(t2, sig_2, linefmt="orange", markerfmt="orange", basefmt="orange")
ass[1,0].axhline(0, color='black', linewidth=0.7)


ass[1,1].plot(t,new_sig_4,color="lime",linestyle="dashed")
ass[1,1].stem(t4, sig_4, linefmt="orange", markerfmt="orange", basefmt="orange")
ass[1,1].axhline(0, color='black', linewidth=0.7)

plt.savefig(f"ex1b&c.pdf", format="pdf", bbox_inches="tight")
plt.show()

# d) Cu cat B este mai mare cu atat functia sinc^2(Bt) seamana mai mult cu un pieptene Dirac
