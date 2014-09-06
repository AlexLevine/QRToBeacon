//
//  iBeaconHandler.h
//  Beaconizer
//
//  Created by Alex Levine on 9/6/14.
//  Copyright (c) 2014 Eliana and Alex and Alex and Alex. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface iBeaconHandler : NSObject

    -(void)SearchForBeacons;

    -(NSString *)ResolveiBeaconWithParse:(NSNumber*) major minorValue:(NSNumber *) minor;
    -(NSArray *)RefreshURLList;




@end
