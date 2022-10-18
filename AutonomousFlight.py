from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

connection_string = "127.0.0.1:14550"

iha = connect(connection_string, wait_ready=True, timeout=100)


i=5
while i>0:
	print("ucus basliyor:",i)
	i=i-1
	time.sleep(1)

def arm_ol_ve_yuksel(hedef_yukseklik):
    while iha.is_armable == False:
        print("Arm ici gerekli sartlar saglanamadi.")
        time.sleep(1)
    print("Iha su anda armedilebilir")

    iha.mode = VehicleMode("GUIDED")
    while iha.mode == 'GUIDED':
        print('Guided moduna gecis yapiliyor')
        time.sleep(1.5)

    print("Guided moduna gecis yapildi")
    iha.armed = True
    while iha.armed is False:
        print("Arm icin bekleniliyor")
        time.sleep(1)

    print("Drone Armed")
    print("Drone Take OFF")

    iha.simple_takeoff(hedef_yukseklik)
    while iha.location.global_relative_frame.alt <= hedef_yukseklik * 0.94:
        print("Su anki yukseklik{}".format(iha.location.global_relative_frame.alt))
        time.sleep(0.5)
    print("Takeoff gerceklesti")



arm_ol_ve_yuksel(5)

time.sleep(10)
	



print("10 Saniye Sonra 1. Kordinata Hareket Edecek ...")
point1 = LocationGlobalRelative( -35.36311264,149.16516789, 5)
iha.simple_goto(point1,airspeed=1)


time.sleep(30)



print("30 Saniye icinde Nokta 2 ye Hareket Edecek...")
point2 = LocationGlobalRelative(-35.36308038,149.16527996 , 5)
iha.simple_goto(point2,airspeed=1)


time.sleep(30)


print("airspeed 1 e sabitlendi")
iha.airspeed = 1


print("30 Saniye icinde Nokta 3 ye Hareket Edecek ")
point3 = LocationGlobalRelative(-35.36325756 ,149.16521631 , 5)
iha.simple_goto(point3,groundspeed=1)


time.sleep(30)


print("drone inis yapiyor")
iha.mode = VehicleMode("LAND")

print("Drone Disarmed")
iha.close()