import numpy as np
import matplotlib.pyplot as plt


def c_calc(first_funct, second_funct):
    return (np.sum(first_funct-np.average(first_funct) * second_funct-np.average(second_funct)) /
            (np.pow(np.sum(np.pow(first_funct-np.average(first_funct),2)),1/2) *
             np.pow(np.sum(np.pow(second_funct-np.average(second_funct),2)),1/2)))


def pade_calc(α_funct):
    return (α_funct - (7 * np.pow(α_funct,3)) / 60) / (1 + np.pow(α_funct,2) / 20)


# pentru α destul de mic sin(α) ≈ α
t = np.arange(-1 * np.pi/2, np.pi/2,step=1/1600)
sin_fun = np.sin(t)

fig, ass = plt.subplots(2)
fig.suptitle('Sin(α) vs α')

ass[0].plot(t,sin_fun)
ass[0].set_title('Sin(α)')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')

ass[1].plot(t,t)
ass[1].set_title('α')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')

plt.savefig("ex8a.pdf", format="pdf", bbox_inches="tight")
plt.show()

plt.plot(t,np.abs(sin_fun-t))
plt.suptitle("Error between sin(α) ≈ α")
plt.savefig("ex8b.pdf", format="pdf", bbox_inches="tight")
plt.show()

pade_values = pade_calc(t)
fig1, ass1 = plt.subplots(2)
fig1.suptitle('Sin(α) vs Pade formula')

ass1[0].plot(t,sin_fun)
ass1[0].set_title('Sin(α)')
ass1[0].set_xlabel('time')
ass1[0].set_ylabel('amplitude')

ass1[1].plot(t,pade_values)
ass1[1].set_title('Pade formula')
ass1[1].set_xlabel('time')
ass1[1].set_ylabel('amplitude')

plt.savefig("ex8c.pdf", format="pdf", bbox_inches="tight")
plt.show()

plt.plot(t,np.abs(sin_fun-pade_values))
plt.suptitle("Error between sin(α) ≈ Pade formula")
plt.savefig("ex8d.pdf", format="pdf", bbox_inches="tight")
plt.show()
