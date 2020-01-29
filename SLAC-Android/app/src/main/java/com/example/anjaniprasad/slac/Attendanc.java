package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class Attendanc extends AppCompatActivity {
TextView tv1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_attendanc);
        Intent iin2= getIntent();
        Bundle b = iin2.getExtras();
tv1= (TextView)findViewById(R.id.att_text);
        if(b!=null)
        {
            String j =(String) b.get("atten");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            tv1.setText(j);
        }
    }
    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Attendanc.this, PostLogin.class);
        Attendanc.this.startActivity(myIntent);
    }
}
