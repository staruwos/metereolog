extern crate linux_embedded_hal as hal;
extern crate bme280;
extern crate rusqlite;
extern crate chrono;

use chrono::prelude::*;
use rusqlite::{Connection, Result, NO_PARAMS};
use std::{thread, time};
use hal::{Delay, I2cdev};
use bme280::BME280;
use std::fs::OpenOptions;
use std::io::prelude::*;

#[derive(Debug)]
struct Infos {
    id: i32,
    date: String,
    infos: String,
}

fn insert_in_db(conn: &mut Connection, infos: &String, date: &String) -> Result<()> 
{
    let tx = conn.transaction()?;

    tx.execute("insert into infos (date, info) values (?1, ?2)", &[date, infos])?;
    tx.commit()
}

fn main() -> Result<()> 
{
    let mut connection = Connection::open("/home/pi/metereolog/metereolog.db")?;
    /*
     * Initialize BME280 and retrieve sensors
     */ 
    // using Linux I2c Bus #1
    let i2c_bus = I2cdev::new("/dev/i2c-1").unwrap();

    // initialize the BME280 using the primary I2C address 0x77
    let mut bme280 = BME280::new_primary(i2c_bus, Delay);

    bme280.init().unwrap();

    let mut measurements = bme280.measure().unwrap();

    while(true)
    {
        //thread::sleep(time::Duration::from_secs(300));
        measurements = bme280.measure().unwrap();
        let mut infos = [measurements.temperature.to_string(), measurements.humidity.to_string(), measurements.pressure.to_string()];

        // truncate informations to use only necessary
        infos[0].truncate(4);
        infos[1].truncate(5);
        infos[2].truncate(5);

        //display_info(&infos); 
        
        // Format string
        let mut text: String = infos[0].to_owned();
        text.push_str(", ");
        text.push_str(&infos[1]);
        text.push_str(", ");
        text.push_str(&infos[2]);
        
        // Retrieve Date and Time
        let local: DateTime<Local> = Local::now();
        let TimeInfo: String = local.format("%m-%-d-%Y, %-I:%M%P").to_string();

        //println!("Time = {}", TimeInfo);
        //println!("Local = {}", local.format("%b %-d %Y, %-I:%M").to_string());

        //save_info_to_file(&text);
        //create_db();

        // Create DB
//        let mut connection = Connection::open("metereolog.db")?;
        insert_in_db(&mut connection, &text, &TimeInfo);
        //connection.execute("INSERT INTO infos (date, info) VALUES (?1, ?2);", &[TimeInfo, text])?; 
        
        println!("Data: {}", TimeInfo);
        println!("T: {}C, U: {}%, P: {}Pa", infos[0], infos[1], infos[2]);  
        println!("------------------------------------");

        thread::sleep(time::Duration::from_secs(300));
    }

//    let mut stmt = connection.prepare("SELECT id, date, info from infos;")?;
//
//    let rows = stmt.query_map(NO_PARAMS, |row| {
//        Infos {
//            id: row.get(0),
//            date: row.get(1),
//            infos: row.get(2),
//        }
//    })?;
//
//    for info in rows {
//        println!("Row = {:?}", info);
//    }

    Ok(())
}

