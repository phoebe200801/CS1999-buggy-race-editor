from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
app = Flask(__name__)

DATABASE_FILE = "database.db"
DEFAULT_BUGGY_ID = "1"

BUGGY_RACE_SERVER_URL = "http://rhul.buggyrace.net"


#------------------------------------------------------------
# the index page
#------------------------------------------------------------
@app.route('/')
def home():
   return render_template('index.html', server_url=BUGGY_RACE_SERVER_URL)

#------------------------------------------------------------
# creating a new buggy:
#  if it's a POST request process the submitted data
#  but if it's a GET request, just show the form
#------------------------------------------------------------
@app.route('/new', methods = ['POST', 'GET'])
def create_buggy():
  if request.method == 'GET':
  
    con = sql.connect(DATABASE_FILE)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM buggies")
    record = cur.fetchone();
  
    return render_template("buggy-form.html", buggy = record)
  elif request.method == 'POST':
  
    con = sql.connect(DATABASE_FILE)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM buggies")
    record = cur.fetchone();
    
    msg=""
    
    qty_wheels = request.form['qty_wheels']
 
    flag_color = request.form['flag_color']
    flag_color_secondary = request.form['flag_color_secondary']
    flag_pattern = request.form['flag_pattern']
 
    power_type = request.form['power_type']
    power_units = request.form['power_units']
    aux_power_type = request.form['aux_power_type']
    aux_power_units = request.form['aux_power_units']
    hamster_booster = request.form['hamster_booster']
 
    tyres = request.form['tyres']
    qty_tyres = request.form['qty_tyres']
 
    armour = request.form['armour']
    fireproof = request.form['fireproof']
    insulated = request.form['insulated']
    antibiotic = request.form['antibiotic']
 
    attack = request.form['attack']
    qty_attacks = request.form['qty_attacks']
 
    banging = request.form['banging']
    algo = request.form['algo']
    
    if int(qty_wheels)%2 != 0:
        msg = f"RULE VIOLATION! PLEASE ENTER AN EVEN INTEGER: Number of Wheels"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        
    if int(qty_tyres) < int(qty_wheels):
        msg = f"RULE VIOLATION! PLEASE ENTER AN INTEGER GREATER THAN", qty_wheels, ": Number of Tyres"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    
    if not qty_wheels.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Number of Wheels"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    elif not power_units.isdigit():
        violations = f"INVALID! PLEASE ENTER AN INTEGER: Units of Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        #units rules validation needed
    elif not aux_power_units.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Units of Auxiliary Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        #units rules validation needed
    elif not hamster_booster.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Hamster Booster"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    elif not qty_tyres.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Number of Tyres"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    elif not qty_attacks.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Number of Attacks"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    
    
    #power costs
    if power_type == "petrol":
        power_cost = int(power_units) * 4
        print("FIXME cost =", power_cost)
    elif power_type == "fusion":
        power_cost = int(power_units) * 400 #needs validation only one unit allowed (1 unit = 100)
        print("FIXME cost =", power_cost)
    elif power_type == "steam":
        power_cost = int(power_units) * 3
        print("FIXME cost =", power_cost)
    elif power_type == "bio":
        power_cost = int(power_units) * 5
        print("FIXME cost =", power_cost)
    elif power_type == "electric":
        power_cost = int(power_units) * 20
        print("FIXME cost =", power_cost)
    elif power_type == "rocket":
        power_cost = int(power_units) * 16
        print("FIXME cost =", power_cost)
    elif power_type == "hamster":
        power_cost = int(power_units) * 3
        print("FIXME cost =", power_cost)
    elif power_type == "themo":
        power_cost = int(power_units) * 300 #1 unit = 100
        print("FIXME cost =", power_cost)
    elif power_type == "solar":
        power_cost = int(power_units) * 40 #1 unit = 30
        print("FIXME cost =", power_cost)
    elif power_type == "wind":
        power_cost = int(power_units) * 20 #1 unit = 30
        print("FIXME cost =", power_cost)
    
    #aux power cost
    if aux_power_type == "petrol":
        aux_power_cost = int(aux_power_units) * 4
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "fusion":
        aux_power_cost = int(aux_power_units) * 400 #1 unit = 100
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "steam":
        aux_power_cost = int(aux_power_units) * 3
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "bio":
        aux_power_cost = int(aux_power_units) * 5
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "electric":
        aux_power_cost = int(aux_power_units) * 20
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "rocket":
        aux_power_cost = int(aux_power_units) * 16
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "hamster":
        aux_power_cost = int(aux_power_units) * 3
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "themo":
        power_cost = int(aux_power_units) * 300 #1 unit = 100
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "solar":
        aux_power_cost = int(aux_power_units) * 40 #1 unit = 30
        print("FIXME cost =", aux_power_cost)
    elif aux_power_type == "wind":
        aux_power_cost = int(aux_power_units) * 20 #1 unit = 30
        print("FIXME cost =", aux_power_cost)
        
    #hamster cost
    hamster_cost = int(hamster_booster) * 5
    print("FIXME hamster =", hamster_cost)
    
    #tyres cost
    if tyres == "knobbly":
        tyres_cost = int(qty_tyres) * 15
        print("FIXME tyres =", tyres_cost)
    elif tyres == "slick":
        tyres_cost = int(qty_tyres) * 10
        print("FIXME tyres =", tyres_cost)
    elif tyres == "steelband":
        tyres_cost = int(qty_tyres) * 20
        print("FIXME tyres =", tyres_cost)
    elif tyres == "reactive":
        tyres_cost = int(qty_tyres) * 40
        print("FIXME tyres =", tyres_cost)
    elif tyres == "maglev":
        tyres_cost = int(qty_tyres) * 50
        print("FIXME tyres =", tyres_cost)
    
    #armour
    if armour == "wood":
        armour_size = (int(qty_wheels)-4) * 10
        print("FIXME size = ", armour_size)
        armour_cost = int(armour_size) * 40
        print("FIXME armour = ", armour_cost)
    elif armour == "aluminimum":
        armour_size = (int(qty_wheels)-4) * 10
        print("FIXME size = ", armour_size)
        armour_cost = int(armour_size) * 200
        print("FIXME armour = ", armour_cost)
    elif armour == "thinsteel":
        armour_size = (int(qty_wheels)-4) * 10
        print("FIXME size = ", armour_size)
        armour_cost = int(armour_size) * 100
        print("FIXME armour = ", armour_cost)
    elif armour == "thicksteel":
        armour_size = (int(qty_wheels)-4) * 10
        print("FIXME size = ", armour_size)
        armour_cost = int(armour_size) * 200
        print("FIXME armour = ", armour_cost)
    elif armour == "titanium":
        armour_size = (int(qty_wheels)-4) * 10
        print("FIXME size = ", armour_size)
        armour_cost = int(armour_size) * 290
        print("FIXME armour = ", armour_cost)
    else:
        armour_cost = 0
        print("FIXME armour = ", armour_cost)
    
    #attack cost
    if attack == "spike":
        attack_cost = int(qty_attacks) * 5
        print("FIXME attack = ", attack_cost)
    elif attack == "flame":
        attack_cost = int(qty_attacks) * 20
        print("FIXME attack = ", attack_cost)
    elif attack == "charge":
        attack_cost = int(qty_attacks) * 28
        print("FIXME attack = ", attack_cost)
    elif attack == "biohazard":
        attack_cost = int(qty_attacks) * 30
        print("FIXME attack = ", attack_cost)
    else:
        attack_cost = 0
        print("FIXME attack = ", attack_cost)
        
    #fireproof cost
    if fireproof == "Yes":
        fireproof_cost = 70
        print("FIXME fireproof =", fireproof_cost)
    else:
        fireproof_cost = 0
        print("FIXME fireproof =", fireproof_cost)
    
    #insulated cost
    if insulated == "Yes":
        insulated_cost = 100
        print("FIXME insulated =", insulated_cost)
    else:
        insulated_cost = 0
        print("FIXME insulated =", insulated_cost)
    
    #antibiotic cost
    if antibiotic == "Yes":
        antibiotic_cost = 90
        print("FIXME antibiotic =", antibiotic_cost)
    else:
        antibiotic_cost = 0
        print("FIXME antibiotic =", antibiotic_cost)
    
    #banging cost
    if banging == "Yes":
        banging_cost = 42
        print("FIXME banging =", banging_cost)
    else:
        banging_cost = 0
        print("FIXME banging =", banging_cost)
        
    total_cost = int(power_cost) + int(aux_power_cost) + int(hamster_cost) + int(tyres_cost) + int(armour_cost) + int(attack_cost) + int(fireproof_cost) + int(insulated_cost) + int(antibiotic_cost) + int(banging_cost)
    print("FIXME total = ", total_cost)
    
    try:
      qty_wheels = request.form['qty_wheels']
      
      flag_color = request.form['flag_color']
      flag_color_secondary = request.form['flag_color_secondary']
      flag_pattern = request.form['flag_pattern']
      
      power_type = request.form['power_type']
      power_units = request.form['power_units']
      aux_power_type = request.form['aux_power_type']
      aux_power_units = request.form['aux_power_units']
      hamster_booster = request.form['hamster_booster']
      
      tyres = request.form['tyres']
      qty_tyres = request.form['qty_tyres']
      
      armour = request.form['armour']
      fireproof = request.form['fireproof']
      insulated = request.form['insulated']
      antibiotic = request.form['antibiotic']
      
      attack = request.form['attack']
      qty_attacks = request.form['qty_attacks']
      
      banging = request.form['banging']
      algo = request.form['algo']
      
      msg = "qty_wheels={qty_wheels}", "flag_color={flag_color}", "flag_color_secondary={flag_color_secondary}", "flag_pattern={flag_pattern}", "power_type={power_type}", "power_units={power_units}", "aux_power_type={aux_power_type}", "aux_power_units={aux_power_units}", "hamster_booster={hamster_booster}", "tyres={tyres}", "qty_tyres={qty_tyres}", "armour={armour}", "fireproof={fireproof}", "insulated={insulated}", "antibiotic={antibiotic}", "attack={attack}", "qty_attacks={qty_attacks}", "banging={banging}", "algo={algo}"
      
      with sql.connect(DATABASE_FILE) as con:
        cur = con.cursor()
        
        cur.execute("UPDATE buggies set qty_wheels=?, flag_color=?, flag_color_secondary=?, flag_pattern=?, power_type=?, power_units=?, aux_power_type=?, aux_power_units=?, hamster_booster=?, tyres=?, qty_tyres=?, armour=?, fireproof=?, insulated=?, antibiotic=?, attack=?, qty_attacks=?, banging=?, algo=?, total_cost=? WHERE id=?", (qty_wheels, flag_color, flag_color_secondary, flag_pattern, power_type, power_units, aux_power_type, aux_power_units, hamster_booster, tyres, qty_tyres, armour, fireproof, insulated, antibiotic, attack, qty_attacks, banging, algo, total_cost, DEFAULT_BUGGY_ID))
        
        con.commit()
        msg = "Record successfully saved"
    except:
      con.rollback()
      msg = "error in update operation"
    finally:
      con.close()
      return render_template("updated.html", msg = msg)

#------------------------------------------------------------
# a page for displaying the buggy
#------------------------------------------------------------
@app.route('/buggy')
def show_buggies():
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies")
  record = cur.fetchone(); 
  return render_template("buggy.html", buggy = record)

#------------------------------------------------------------
# a page for displaying the buggy
#------------------------------------------------------------
@app.route('/new')
def edit_buggy():
  return render_template("buggy-form.html")


#------------------------------------------------------------
# get JSON from current record
#   this is still probably right, but we won't be
#   using it because we'll be dipping diectly into the
#   database
#------------------------------------------------------------
@app.route('/json')
def summary():
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies WHERE id=? LIMIT 1", (DEFAULT_BUGGY_ID))
  return jsonify(
      {k: v for k, v in dict(zip(
        [column[0] for column in cur.description], cur.fetchone())).items()
        if (v != "" and v is not None)
      }
    )

#------------------------------------------------------------
# delete the buggy
#   don't want DELETE here, because we're anticipating
#   there always being a record to update (because the
#   student needs to change that!)
#------------------------------------------------------------
@app.route('/delete', methods = ['POST'])
def delete_buggy():
  try:
    msg = "deleting buggy"
    with sql.connect(DATABASE_FILE) as con:
      cur = con.cursor()
      cur.execute("DELETE FROM buggies")
      con.commit()
      msg = "Buggy deleted"
  except:
    con.rollback()
    msg = "error in delete operation"
  finally:
    con.close()
    return render_template("updated.html", msg = msg)


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")
