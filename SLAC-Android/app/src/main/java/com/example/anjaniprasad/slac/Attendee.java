package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class Attendee extends AppCompatActivity {
TextView tva;
String name,g;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_attendee);
        Intent iint= getIntent();
        Bundle b = iint.getExtras();
        tva=(TextView)findViewById(R.id.atten_text);

        if(b!=null)
        {
            String j =b.getString("attend");
            name=b.getString("name");
            if(j.equalsIgnoreCase("pr")) {
                g = "Attendance given in last class";//
            }
            else {
                g="Attendance wasn't given in the last class";
            }
            tva.setText(g);
        }
    }

    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Attendee.this, PostLogin1.class);
        myIntent.putExtra("name",name);
        Attendee.this.startActivity(myIntent);
    }
}
