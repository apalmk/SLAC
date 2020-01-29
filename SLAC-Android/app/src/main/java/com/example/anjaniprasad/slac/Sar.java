package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class Sar extends AppCompatActivity {
TextView tvb;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sar);
        tvb=(TextView)findViewById(R.id.sar_text);
        Intent iin5= getIntent();
        Bundle b = iin5.getExtras();

        if(b!=null)
        {
            String j =(String) b.get("sa");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            tvb.setText(j);
        }
    }
    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Sar.this, PostLogin.class);
        Sar.this.startActivity(myIntent);
    }
}
