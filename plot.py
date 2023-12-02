import matplotlib.pyplot as plt


x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]



ylmm1 = [0.1115, 0.2518, 0.4206, 0.6585, 1.0045, 1.5090, 2.3333, 3.9848]
ylqmm1 = [0.01119, 0.0492, 0.1278, 0.2668, 0.5026, 0.9054, 1.6422, 3.2161]

ywmm1 = [1.1125, 1.2408, 1.4274, 1.6554, 2.0107, 2.5258, 3.2831, 4.9976]
ywqmm1 = [0.1119, 0.2467, 0.4289, 0.6699, 1.0049, 1.5105, 2.3376, 3.9976]

ylmm1theo = [0.1111, 0.25, 0.42857, 0.6667, 1, 1.5, 2.3333, 4]
ylqmm1theo = [0.01111, 0.05, 0.12857, 0.2667, 0.5, 0.9, 1.6333, 3.2]

ywmm1theo = [1.1111, 1.25, 1.42857, 1.6667, 2, 2.5, 3.3333, 5]
ywqmm1theo = [0.1111, 0.25, 0.42857, 0.6667, 1, 1.5,  2.3333, 4]




ylmg1 = [0.1068, 0.2338, 0.3830, 0.5728, 0.8334, 1.2191, 1.8069, 2.9749]
ylqmg1 = [0.0074, 0.0336, 0.0845, 0.1770, 0.3322, 0.6051, 1.0911, 2.1272]

ywmg1 = [1.0722, 1.1636, 1.2772, 1.4304, 1.6545, 2.0132, 2.5621, 3.6582]
ywqmg1 = [0.0741, 0.1685, 0.2849, 0.4440, 0.6647, 1.0003, 1.5592, 2.6781]

ylmg1theo = [0.1074, 0.2333, 0.3857, 0.5778, 0.8333, 1.2, 1.7889, 2.9333]
ylqmg1theo = [0.0074, 0.03333, 0.0857, 0.1778, 0.3333, 0.6, 1.0889, 2.1333]

ywmg1theo = [1.0741, 1.1667, 1.2857, 1.4444, 1.6667, 2, 2.5556, 3.6667]
ywqmg1theo = [0.0741, 0.1667, 0.2857, 0.4444, 0.6667, 1, 1.5556, 2.6667]




ylmmcn = [0.3025, 0.6087, 0.9215, 1.2792, 1.7268, 2.3409, 3.1997,4.6799, ]
ylqmmcn = [0.000426, 0.00608, 0.03009, 0.0935, 0.2350, 0.5407, 1.0884, 2.3752]

ywmmcn = [0.9995, 1.0079, 1.0305, 1.0660, 1.1529, 1.3091, 1.5222, 1.9668]
ywqmmcn = [0.00142, 0.0101, 0.0339, 0.0785, 0.1575, 0.2974, 0.5201, 0.9838]

ylmmcntheo = [0.3004, 0.6063, 0.9316, 1.3028, 1.7686, 2.4192, 3.4210, 5.1165]
ylqmmcntheo = [0.0004, 0.0063, 0.0316, 0.1028, 0.2686, 0.6193, 1.3306, 2.7247]

ywmmcntheo = [1.0014, 1.0105, 1.0351, 1.0857, 1.1791, 1.3441, 1.6339, 2.1392]
ywqmmcntheo = [0.00138, 0.0105, 0.0350, 0.0857, 0.1790, 0.3441, 0.6339, 1.1392]




ys1network = [2.1364, 2.3181, 2.5347, 2.8045, 3.1916, 3.7270, 4.5770, 6.3543]

ys2network = [2.1741, 2.4094, 2.7026, 3.0453, 3.5612, 4.2448, 5.2676, 7.3127]



ys1networktheo = [2.1420, 2.3138, 2.5275, 2.8030, 3.1765, 3.7195, 4.5992, 6.3158]

ys2networktheo = [2.1864, 2.4128, 2.6944, 3.0556, 3.5385, 4.2241, 5.2941, 7.2727]

pn = [3.3444816053511686e-18, 2.637558412521046e-12, 6.656790123454948e-09, 1.5899108149426105e-06, 0.00010248461421261183, 0.0027992283689701304, 0.04036921023468757, 0.3405057079364419]


data = [ylmm1, ylqmm1, ywmm1, ywqmm1, ylmg1, ylqmg1, ywmg1, ywqmg1, ylmmcn, ylqmmcn, ywmmcn, ywqmmcn, ys1network, ys2network]
w, h = 8, 14
err = [[0 for i in range(w)] for j in range(h)]
for i in range(len(data)):
    for j in range(len(data[i])):
        if ((i == 12 or i == 13) and j == 7):
            err[i][j] = 0.03 * data[i][j]
        else:
            err[i][j] = 0.01 * data[i][j]




plt.title("L & Lq for M/M/1 Queue")
plt.xlabel("Utilization (rho)")
plt.ylabel("Number of Customers")
plt.errorbar(x, ylmm1, yerr = err[0], label="L")
plt.errorbar(x, ylqmm1, yerr = err[1], label="Lq")
plt.errorbar(x, ylmm1theo, label="L Theoretical")
plt.errorbar(x,  ylqmm1theo, label="Lq Theoretical")
plt.legend()
plt.show()


plt.title("W & Wq for M/M/1 Queue")
plt.xlabel("Utilization (rho)")
plt.ylabel("Time Spent (minutes)")
plt.errorbar(x, ywmm1, yerr = err[2], label="W")
plt.errorbar(x, ywqmm1, yerr = err[3], label="Wq")
plt.errorbar(x, ywmm1theo, label="W Theoretical")
plt.errorbar(x, ywqmm1theo, label="Wq Theoretical")
plt.legend()
plt.show()




plt.title("L & Lq for M/G/1 Queue")
plt.xlabel("Utilization (rho)")
plt.ylabel("Number of Customers")
plt.errorbar(x, ylmg1, yerr = err[4], label="L")
plt.errorbar(x, ylqmg1, yerr = err[5], label="Lq")
plt.errorbar(x, ylmg1theo, label="L Theoretical")
plt.errorbar(x, ylqmg1theo, label="Lq Theoretical")
plt.legend()
plt.show()




plt.title("W & Wq for M/G/1 Queue")
plt.xlabel("Utilization (rho)")
plt.ylabel("Time Spent (minutes)")
plt.errorbar(x, ywmg1, yerr = err[6], label="W")
plt.errorbar(x, ywqmg1, yerr = err[7], label="Wq")
plt.errorbar(x, ywmg1theo, label="W Theoretical")
plt.errorbar(x, ywqmg1theo, label="Wq Theoretical")
plt.legend()
plt.show()








plt.title("L & Lq for M/M/c/N Queue")
plt.xlabel("Utilization (rho)")
plt.ylabel("Number of Customers")
plt.errorbar(x, ylmmcn, yerr = err[8], label="L")
plt.errorbar(x, ylqmmcn, yerr = err[9], label="Lq")
plt.errorbar(x, ylmmcntheo, label="L Theoretical")
plt.errorbar(x, ylqmmcntheo, label="Lq Theoretical")
plt.legend()
plt.show()





plt.title("W & Wq for M/M/c/N Queue")
plt.xlabel("Utilization (rho)")
plt.ylabel("Time Spent (minutes)")
plt.errorbar(x, ywmmcn, yerr = err[10], label="W")
plt.errorbar(x, ywqmmcn, yerr = err[11], label="Wq")
plt.errorbar(x, ywmmcntheo, label="W Theoretical")
plt.errorbar(x, ywqmmcntheo, label="Wq Theoretical")
plt.legend()
plt.show()


plt.title("Probablility of Loss for M/M/c/N Queue")
plt.xlabel("Utilization (rho)")
plt.ylabel("Probablility (%)")
plt.errorbar(x, pn, label="Pn")
plt.legend()
plt.show()


plt.title("Response Time in Network of Queues")
plt.xlabel("Utilization (rho)")
plt.ylabel("Response Time (minutes)")
plt.errorbar(x, ys1network, yerr = err[12], label="Stream 1")
plt.errorbar(x, ys2network, yerr = err[13], label="Stream 2")
plt.errorbar(x, ys1networktheo, label="Stream 1 Theoretical")
plt.errorbar(x, ys2networktheo, label="Stream 2 Theoretical")
plt.legend()
plt.show()
