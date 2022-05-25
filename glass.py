from cmath import nan
import math
import os


class SpectralLine:
    t = 1013.980
    s =  852.110
    r =  706.519
    C =  656.273
    C_=  643.847
    D =  589.294
    d =  587.562
    e =  546.074
    F =  486.133
    F_=  479.991
    g =  435.834
    h =  404.656
    i =  365.015


class DispersionFormula:
    @staticmethod
    # Zemax
    def Schott(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2) + c[2]*pow(lambdamicron,-2) + c[3]*pow(lambdamicron,-4) + c[4]*pow(lambdamicron,-6) + c[5]*pow(lambdamicron,-8) )

    def Sellmeier1(lambdamicron, c:list):
        return math.sqrt( 1 + c[0]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[1]) + c[2]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[3]) + c[4]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[5]) )

    def Sellmeier2(lambdamicron, c:list):
        return math.sqrt( 1 + c[0] + c[1]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[2]) + c[3]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[4]) )

    def Sellmeier3(lambdamicron, c:list):
        return math.sqrt( 1 + c[0]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[1]) + c[2]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[3]) + c[4]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[5]) + c[6]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[7]) )

    def Sellmeier4(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[2]) + c[3]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[4]) )

    def Sellmeier5(lambdamicron, c:list):
        return math.sqrt( 1 + c[0]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[1]) + c[2]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[3]) + c[4]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[5]) + c[6]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[7]) + c[8]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[9]) )

    def Herzberger(lambdamicron, c:list):
        L = 1/(pow(lambdamicron,2)-0.028)
        return ( c[0] + c[1]*L + c[2]*pow(L,2) + c[3]*pow(lambdamicron,2) + c[4]*pow(lambdamicron,4) + c[5]*pow(lambdamicron,6) )

    def HandbookOfOptics1(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]/(pow(lambdamicron,2)-c[2]) - c[3]*pow(lambdamicron,2) )

    def HandbookOfOptics2(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[2]) - c[3]*pow(lambdamicron,2) )

    def Extended1(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2) + c[2]*pow(lambdamicron,-2) + c[3]*pow(lambdamicron,-4) + c[4]*pow(lambdamicron,-6) + c[5]*pow(lambdamicron,-8) + c[6]*pow(lambdamicron,-10) + c[7]*pow(lambdamicron,-12) )

    def Extended2(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2) + c[2]*pow(lambdamicron,-2) + c[3]*pow(lambdamicron,-4) + c[4]*pow(lambdamicron,-6) + c[5]*pow(lambdamicron,-8) + c[6]*pow(lambdamicron,4) + c[7]*pow(lambdamicron,6) )

    def Conrady(lambdamicron, c:list):
        return ( c[0] + c[1]/lambdamicron + c[2]/pow(lambdamicron,3.5) )

    def NikonHikari(lambdamicron, c:list):
        # https://www.hikari-g.co.jp/products/nature/properties_optical_glass/
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2) + c[2]*pow(lambdamicron,4) + c[3]*pow(lambdamicron,-2) + c[4]*pow(lambdamicron,-4) + c[5]*pow(lambdamicron,-6) + c[6]*pow(lambdamicron,-8) + c[7]*pow(lambdamicron,-10) + c[8]*pow(lambdamicron, -12) )

    # CodeV
    def Laurent(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2) + c[2]*pow(lambdamicron,-2) + c[3]*pow(lambdamicron,-4) + c[4]*pow(lambdamicron,-6) + c[5]*pow(lambdamicron,-8) + c[6]*pow(lambdamicron,-10) + c[7]*pow(lambdamicron,-12) + c[8]*pow(lambdamicron,-14) + c[9]*pow(lambdamicron,-16) + c[10]*pow(lambdamicron,-18) + c[11]*pow(lambdamicron,-20) )

    def GlassManufacturerLaurent(lambdamicron, c:list):
        return math.sqrt( c[0] + c[1]*pow(lambdamicron,2) + c[2]*pow(lambdamicron,-2) + c[3]*pow(lambdamicron,-4) + c[4]*pow(lambdamicron,-6) + c[5]*pow(lambdamicron,-8) + c[6]*pow(lambdamicron,4) )

    def GlassManufacturerSellmeier(lambdamicron, c:list):
        return math.sqrt( 1 + c[0]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[1]) + c[2]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[3]) + c[4]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[5]) + c[6]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[7]) + c[8]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[9]) + c[10]*pow(lambdamicron,2)/(pow(lambdamicron,2)-c[11]) )

    def StandardSellmeier(lambdamicron, c:list):
        return math.sqrt( 1 + c[0]*pow(lambdamicron,2)/(pow(lambdamicron,2)-pow(c[1],2)) + c[2]*pow(lambdamicron,2)/(pow(lambdamicron,2)-pow(c[3],2)) + c[4]*pow(lambdamicron,2)/(pow(lambdamicron,2)-pow(c[5],2)) + c[6]*pow(lambdamicron,2)/(pow(lambdamicron,2)-pow(c[7],2)) + c[8]*pow(lambdamicron,2)/(pow(lambdamicron,2)-pow(c[9],2)) + c[10]*pow(lambdamicron,2)/(pow(lambdamicron,2)-pow(c[11],2)) )

    def Cauchy(lambdamicron, c:list):
        return c[0] + c[1]*pow(lambdamicron,-2) + c[2]*pow(lambdamicron,-4)

    def Hartman(lambdamicron, c:list):
        return c[0] + c[1]/pow((c[2]-lambdamicron), 1.2)


class Air:
    def __init__(self) -> None:
        pass

    def refractive_index_ref(self,lambdamicron) -> float:
        term1 = 6432.8
        term2 = 2949810.0*pow(lambdamicron, 2)/( 146.0*pow(lambdamicron,2) - 1.0 )
        term3 = 25540.0*pow(lambdamicron,2)/( 41.0*pow(lambdamicron,2) - 1.0 )
        nref = 1.0 + (term1 + term2 + term3)*pow(10, -8)
        return nref

    def refractive_index_abs(self, lambdamicron, T:float, P= 101325.0) -> float:
        P0 = 101325.0
        Tref = 15
        nref = self.refractive_index_ref(lambdamicron)
        num = nref - 1.0
        denom =  1.0 + (T-Tref)*(3.4785*pow(10,-3))
        return ( 1.0 + (num/denom)*(P/P0) )


class Glass:
    def __init__(self) -> None:
        self.T :float = 20
        self.Tref :float = 20

        self.comment :str = ""
        self.product_name :str = ""
        self.supplier :str = ""
        
        self.dispersion_coefs :list[float] = [0.0 for i in range(10)]
        self.formula_index :int = 1

        self.has_thermal_data :bool = True
        self.D0 = 0.0
        self.D1 = 0.0
        self.D2 = 0.0
        self.E0 = 0.0
        self.E1 = 0.0
        self.Ltk = 0.0

    def refractive_index(self, lambdamicron) -> float:
        return self.refractive_index_rel(lambdamicron)

    def abbe_d(self) -> float:
        nd = self.refractive_index(SpectralLine.d/1000.0)
        nF = self.refractive_index(SpectralLine.F/1000.0)
        nC = self.refractive_index(SpectralLine.C/1000.0)
        return (nd - 1.0)/(nF - nC)
        
    def refractive_index_rel_Tref(self, lambdamicron) -> float:
        if  ( 1 == self.formula_index ):
            return DispersionFormula.Schott(lambdamicron, self.dispersion_coefs)
        elif( 2 == self.formula_index ):
            return DispersionFormula.Sellmeier1(lambdamicron, self.dispersion_coefs)
        elif( 3 == self.formula_index ):
            return DispersionFormula.Herzberger(lambdamicron, self.dispersion_coefs)
        elif( 4 == self.formula_index ):
            return DispersionFormula.Sellmeier2(lambdamicron, self.dispersion_coefs)
        elif( 5 == self.formula_index ):
            return DispersionFormula.Conrady(lambdamicron, self.dispersion_coefs)
        elif( 6 == self.formula_index ):
            return DispersionFormula.Sellmeier3(lambdamicron, self.dispersion_coefs)
        elif( 7 == self.formula_index ):
            return DispersionFormula.HandbookOfOptics1(lambdamicron, self.dispersion_coefs)
        elif( 8 == self.formula_index ):
            return DispersionFormula.HandbookOfOptics2(lambdamicron, self.dispersion_coefs)
        elif( 9 == self.formula_index ):
            return DispersionFormula.Sellmeier4(lambdamicron, self.dispersion_coefs)
        elif( 10 == self.formula_index ):
            return DispersionFormula.Extended1(lambdamicron, self.dispersion_coefs)
        elif( 11 == self.formula_index ):
            return DispersionFormula.Sellmeier5(lambdamicron, self.dispersion_coefs)
        elif( 12 == self.formula_index ):
            return DispersionFormula.Extended2(lambdamicron, self.dispersion_coefs)
        elif( 13 == self.formula_index ):
            return nan
        else:
            return nan


    def refractive_index_abs_Tref(self, lambdamicron) ->float:
        P = 101325.0
        air = Air()
        n_air_T0 = air.refractive_index_abs(lambdamicron, self.Tref, P)
        n_rel_T0 = self.refractive_index_rel_Tref(lambdamicron)
        n_abs_T0 = n_rel_T0*n_air_T0
        return n_abs_T0

    def refractive_index_abs(self, lambdamicron) ->float:
        dn = 0.0
        if(self.has_thermal_data):
            dn_dt = self.dn_dt_abs(self.T, lambdamicron)
            dn = (self.T - self.Tref)*dn_dt

        n_abs_T0 = self.refractive_index_abs_Tref(lambdamicron)
        n_abs = n_abs_T0 + dn
        return n_abs
    
    def refractive_index_rel(self, lambdamicron) ->float:
        air = Air()
        n_abs = self.refractive_index_abs(lambdamicron)
        n_air = air.refractive_index_abs(lambdamicron, self.T)
        n_rel = n_abs/n_air
        return n_rel

    def dn_dt_abs(self, T:float, lambdamicron) -> float:
        dT = T - self.Tref
        Stk = (self.Ltk > 0.0) - (self.Ltk < 0.0)
        n = self.refractive_index_abs_Tref(lambdamicron)
        return (n*n-1)/(2*n) * ( self.D0 + 2*self.D1*dT + 3*self.D2*dT*dT + (self.E0 + 2*self.E1*dT)/(lambdamicron*lambdamicron - Stk*self.Ltk*self.Ltk) )


class GlassCatalog:
    def __init__(self) -> None:
        self.supplier : str = ""
        self.glasses = []

    def set_temperature(self, t):
        for g in self.glasses:
            g.T = t

    def load_agf(self, agf_path) -> bool:
        self.glasses.clear()
        self.supplier = os.path.splitext(os.path.basename(agf_path))[0]

        file = open(agf_path, 'r')
        lines = file.readlines()

        for line in lines:
            if line.startswith('NM'):
                lineparts = line.rstrip().split()
                g = Glass()
                self.glasses.append(g)
                self.glasses[-1].supplier = self.supplier
                self.glasses[-1].product_name = lineparts[1]
                self.glasses[-1].formula_index = int(float(lineparts[2]))

                if 13 == self.glasses[-1].formula_index:
                    pass
                    #print("     Unknown dispersion formula")

            elif line.startswith('GC'):
                self.glasses[-1].comment = line.lstrip('GC')
            elif line.startswith('CD'):
                lineparts = line.rstrip().split()
                num_coefs = len(lineparts)
                for i in range(1, num_coefs):
                    self.glasses[-1].dispersion_coefs[i-1] = float(lineparts[i])
            elif line.startswith('TD'):
                lineparts = line.rstrip().split()
                if 8 == len(lineparts):
                    self.glasses[-1].has_thermal_data = True
                    self.glasses[-1].D0 = float(lineparts[1])
                    self.glasses[-1].D1 = float(lineparts[2])
                    self.glasses[-1].D2 = float(lineparts[3])
                    self.glasses[-1].E0 = float(lineparts[4])
                    self.glasses[-1].E1 = float(lineparts[5])
                    self.glasses[-1].Ltk = float(lineparts[6])
                    self.glasses[-1].Tref = float(lineparts[7])
                else:
                    self.glasses[-1].has_thermal_data = False
                    #print("     Thermal data not contained")

        file.close()

        return True



class GlassCatalogManager:
    def __init__(self) -> None:
        self.catalogs = []
    
    def set_temperature(self, t):
        for c in self.catalogs:
            c.set_temperature(t)
    
    def load_agf_files(self, agf_paths) -> None:
        self.catalogs.clear()
        for filepath in agf_paths:
            catalog = GlassCatalog()
            ok = catalog.load_agf(filepath)
            if ok:
                print("Loaded " + filepath)
                self.catalogs.append(catalog)

    

