from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/mensaje')
def validate_user():
    return jsonify()


if __name__ == '__main__':
    app.run(debug=True)


#@app.post("/locations/{name}/{lat}/{lon}", response_model=schemas.Location)
#def add_location(datos: schemas.Location, db: Session = Depends(get_db)):
#    location = models.Location(name = datos.name, lat = datos.lat, lon = datos.lon)
#    db.add(location)
#    db.commit()
#    db.refresh(location)
#    return location