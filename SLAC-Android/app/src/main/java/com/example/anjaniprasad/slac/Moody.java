package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class Moody extends AppCompatActivity {
TextView tvm;
String name;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_moody);
        tvm= (TextView)findViewById(R.id.moody_text);
        Intent iino= getIntent();
        Bundle b = iino.getExtras();
        if(b!=null)
        {
            String j =b.getString("moodd");
            name=b.getString("name");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            tvm.setText(j);
        }
    }

    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Moody.this, PostLogin1.class);
        myIntent.putExtra("name",name);
        Moody.this.startActivity(myIntent);
    }
}
