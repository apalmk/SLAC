package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class Ear extends AppCompatActivity {
TextView tv2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ear);
        tv2=(TextView)findViewById(R.id.lcel_text);
        Intent iin2= getIntent();
        Bundle b = iin2.getExtras();

        if(b!=null)
        {
            String j =(String) b.get("lcel");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            tv2.setText(j);
        }
    }
    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Ear.this, PostLogin.class);
        Ear.this.startActivity(myIntent);
    }
}
